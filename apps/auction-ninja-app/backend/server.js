import express from 'express';
import cors from 'cors';
import puppeteer from 'puppeteer';
import NodeCache from 'node-cache';

const app = express();
const PORT = 3001;

// Cache auction data for 5 minutes
const cache = new NodeCache({ stdTTL: 300 });

// Keep a browser instance for better performance
let browser = null;

app.use(cors());
app.use(express.json());

// Initialize browser
async function getBrowser() {
  if (!browser) {
    console.log('Launching browser...');
    browser = await puppeteer.launch({
      headless: 'new',
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-web-security'
      ]
    });
  }
  return browser;
}

// Helper function to calculate distance between two coordinates using Haversine formula
function calculateDistance(lat1, lon1, lat2, lon2) {
  const R = 3959; // Earth's radius in miles
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

// Helper function to get coordinates for a ZIP code
async function getCoordinatesForZip(zipCode) {
  try {
    // Using a free geocoding service with native fetch
    const response = await fetch(`https://api.zippopotam.us/us/${zipCode}`);
    if (response.ok) {
      const data = await response.json();
      if (data && data.places && data.places[0]) {
        return {
          lat: parseFloat(data.places[0].latitude),
          lon: parseFloat(data.places[0].longitude)
        };
      }
    }
  } catch (error) {
    console.error('Error fetching coordinates for ZIP:', error.message);
  }
  return null;
}

// Extract ZIP code from location string
function extractZipCode(locationString) {
  // Try to extract a 5-digit ZIP code from the location string
  const zipMatch = locationString.match(/\b\d{5}\b/);
  return zipMatch ? zipMatch[0] : null;
}

// Parse relative time strings (e.g., "Ends in 3 hours", "2h 30m", etc.)
function parseRelativeTime(timeString) {
  const now = new Date();

  // Try to extract hours and minutes
  const hoursMatch = timeString.match(/(\d+)\s*h/i);
  const minutesMatch = timeString.match(/(\d+)\s*m/i);
  const daysMatch = timeString.match(/(\d+)\s*d/i);

  let totalMinutes = 0;

  if (daysMatch) totalMinutes += parseInt(daysMatch[1]) * 24 * 60;
  if (hoursMatch) totalMinutes += parseInt(hoursMatch[1]) * 60;
  if (minutesMatch) totalMinutes += parseInt(minutesMatch[1]);

  if (totalMinutes > 0) {
    return new Date(now.getTime() + totalMinutes * 60 * 1000);
  }

  // Try to parse as a date
  try {
    const date = new Date(timeString);
    if (!isNaN(date.getTime())) {
      return date;
    }
  } catch (error) {
    console.error('Error parsing time:', error);
  }

  return null;
}

// Fetch auctions from AuctionNinja using Puppeteer
async function fetchAuctionNinjaData() {
  const cachedData = cache.get('auctions');
  if (cachedData) {
    console.log('Returning cached auction data');
    return cachedData;
  }

  let page = null;

  try {
    console.log('Fetching fresh auction data with Puppeteer...');

    const browserInstance = await getBrowser();
    page = await browserInstance.newPage();

    // Set viewport for consistent rendering
    await page.setViewport({ width: 1920, height: 1080 });

    // Set user agent to appear as a normal browser
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

    console.log('Navigating to AuctionNinja auctions page...');
    await page.goto('https://www.auctionninja.com/auctions', {
      waitUntil: 'networkidle2',
      timeout: 30000
    });

    console.log('Page loaded, waiting for content...');

    // Wait a bit for any dynamic content to load
    await page.waitForTimeout(2000);

    // Try to find auction listings - we'll need to inspect the actual page structure
    // For now, let's extract all links and content that looks like auctions
    const auctions = await page.evaluate(() => {
      const results = [];

      // Try various selectors that might contain auctions
      const possibleSelectors = [
        'article',
        '[class*="auction"]',
        '[class*="listing"]',
        '[class*="item"]',
        '.card',
        '[class*="card"]'
      ];

      let elements = [];
      for (const selector of possibleSelectors) {
        const found = document.querySelectorAll(selector);
        if (found.length > 0 && found.length < 100) { // Reasonable number of items
          elements = Array.from(found);
          console.log(`Found ${elements.length} elements with selector: ${selector}`);
          break;
        }
      }

      // If no structured elements, look for links to individual auctions
      if (elements.length === 0) {
        const links = document.querySelectorAll('a[href*="auction"]');
        elements = Array.from(links).map(link => link.closest('div, article, li, tr') || link);
      }

      elements.forEach((elem, index) => {
        try {
          // Extract text content
          const text = elem.textContent || '';

          // Find title - usually in heading or strong element
          let title = '';
          const heading = elem.querySelector('h1, h2, h3, h4, h5, h6, strong, [class*="title"], [class*="name"]');
          if (heading) {
            title = heading.textContent.trim();
          } else {
            // Use first substantial text
            const words = text.split(/\s+/).filter(w => w.length > 2);
            title = words.slice(0, 10).join(' ');
          }

          // Find link
          let link = '';
          const anchor = elem.querySelector('a') || (elem.tagName === 'A' ? elem : null);
          if (anchor) {
            link = anchor.href;
          }

          // Find image
          let image = '';
          const img = elem.querySelector('img');
          if (img) {
            image = img.src;
          }

          // Extract location (look for state abbreviations, ZIP codes)
          let location = '';
          const locationMatch = text.match(/([A-Z][a-z]+,?\s*[A-Z]{2}\s*\d{5})|([A-Z][a-z]+,?\s*[A-Z]{2})/);
          if (locationMatch) {
            location = locationMatch[0];
          }

          // Extract time information
          let endTime = '';
          const timeMatch = text.match(/(ends?\s+in\s+[\d\s\w]+)|(closing\s+[\d\s\w]+)|([\d]+\s*h\s*[\d]*\s*m?)/i);
          if (timeMatch) {
            endTime = timeMatch[0];
          }

          // Extract item count
          let items = null;
          const itemsMatch = text.match(/(\d+)\s*items?/i);
          if (itemsMatch) {
            items = parseInt(itemsMatch[1]);
          }

          if (title && title.length > 5) {
            results.push({
              id: index,
              title: title.substring(0, 200),
              location,
              endTime,
              link,
              image,
              items,
              rawText: text.substring(0, 500)
            });
          }
        } catch (error) {
          console.error('Error extracting auction data:', error);
        }
      });

      return results;
    });

    console.log(`Extracted ${auctions.length} potential auctions from page`);

    // Process the extracted data
    const processedAuctions = [];

    for (const auction of auctions) {
      // Parse end time
      let endTime = null;
      if (auction.endTime) {
        endTime = parseRelativeTime(auction.endTime);
      }

      // If we couldn't parse the time, skip or use a default
      if (!endTime) {
        // Default to 12 hours from now for items without clear end times
        endTime = new Date(Date.now() + 12 * 60 * 60 * 1000);
      }

      // Extract ZIP code from location
      const zipCode = auction.location ? extractZipCode(auction.location) : null;

      processedAuctions.push({
        ...auction,
        endTime: endTime.toISOString(),
        zipCode,
        category: inferCategory(auction.title)
      });
    }

    console.log(`Processed ${processedAuctions.length} auctions`);

    if (processedAuctions.length > 0) {
      cache.set('auctions', processedAuctions);
      return processedAuctions;
    }

    // If no auctions found, return mock data
    console.log('No auctions extracted, returning mock data for development');
    return getMockAuctions();

  } catch (error) {
    console.error('Error fetching auction data with Puppeteer:', error.message);
    console.error('Stack:', error.stack);
    // Return mock data if fetching fails
    return getMockAuctions();
  } finally {
    if (page) {
      await page.close();
    }
  }
}

// Infer category from title
function inferCategory(title) {
  const lower = title.toLowerCase();

  if (lower.match(/furniture|chair|table|couch|sofa|desk/)) return 'Furniture';
  if (lower.match(/tool|equipment|machinery|hardware/)) return 'Tools';
  if (lower.match(/jewelry|ring|necklace|watch|bracelet/)) return 'Jewelry';
  if (lower.match(/art|painting|sculpture|print/)) return 'Art';
  if (lower.match(/electronic|computer|laptop|phone|tv|audio/)) return 'Electronics';
  if (lower.match(/antique|vintage|collectible|estate/)) return 'Collectibles';
  if (lower.match(/restaurant|kitchen|commercial/)) return 'Equipment';
  if (lower.match(/vehicle|car|truck|motorcycle|auto/)) return 'Vehicles';

  return 'Other';
}

// Mock auction data for development/testing
function getMockAuctions() {
  const now = new Date();
  const in12Hours = new Date(now.getTime() + 12 * 60 * 60 * 1000);
  const in18Hours = new Date(now.getTime() + 18 * 60 * 60 * 1000);
  const in30Hours = new Date(now.getTime() + 30 * 60 * 60 * 1000);

  return [
    {
      id: 1,
      title: 'Estate Sale - Antique Furniture Collection',
      location: 'Norwalk, CT 06851',
      zipCode: '06851',
      lat: 41.1175,
      lon: -73.4079,
      endTime: in12Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/1',
      image: 'https://via.placeholder.com/400x300?text=Antique+Furniture',
      items: 45,
      category: 'Furniture'
    },
    {
      id: 2,
      title: 'Tool Liquidation Auction',
      location: 'Stamford, CT 06902',
      zipCode: '06902',
      lat: 41.0534,
      lon: -73.5387,
      endTime: in18Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/2',
      image: 'https://via.placeholder.com/400x300?text=Tools',
      items: 127,
      category: 'Tools'
    },
    {
      id: 3,
      title: 'Vintage Jewelry & Collectibles',
      location: 'Darien, CT 06820',
      zipCode: '06820',
      lat: 41.0787,
      lon: -73.4693,
      endTime: in12Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/3',
      image: 'https://via.placeholder.com/400x300?text=Jewelry',
      items: 89,
      category: 'Jewelry'
    },
    {
      id: 4,
      title: 'Restaurant Equipment Sale',
      location: 'New Canaan, CT 06840',
      zipCode: '06840',
      lat: 41.1468,
      lon: -73.4948,
      endTime: in18Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/4',
      image: 'https://via.placeholder.com/400x300?text=Restaurant+Equipment',
      items: 63,
      category: 'Equipment'
    },
    {
      id: 5,
      title: 'Art Gallery Liquidation',
      location: 'Greenwich, CT 06830',
      zipCode: '06830',
      lat: 41.0262,
      lon: -73.6282,
      endTime: in30Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/5',
      image: 'https://via.placeholder.com/400x300?text=Art',
      items: 34,
      category: 'Art'
    },
    {
      id: 6,
      title: 'Electronics & Computer Equipment',
      location: 'Westport, CT 06880',
      zipCode: '06880',
      lat: 41.1415,
      lon: -73.3579,
      endTime: in12Hours.toISOString(),
      link: 'https://www.auctionninja.com/auction/6',
      image: 'https://via.placeholder.com/400x300?text=Electronics',
      items: 156,
      category: 'Electronics'
    }
  ];
}

// API endpoint to get filtered auctions
app.get('/api/auctions', async (req, res) => {
  try {
    const { zipCode = '06870', radius = 20, hours = 24 } = req.query;

    console.log(`Fetching auctions for ZIP ${zipCode}, radius ${radius} miles, ending in ${hours} hours`);

    // Get coordinates for the target ZIP code
    const targetCoords = await getCoordinatesForZip(zipCode);
    if (!targetCoords) {
      return res.status(400).json({ error: 'Invalid ZIP code' });
    }

    // Fetch all auctions
    const allAuctions = await fetchAuctionNinjaData();

    // Get current time and calculate cutoff
    const now = new Date();
    const cutoffTime = new Date(now.getTime() + parseInt(hours) * 60 * 60 * 1000);

    // Filter auctions by location and time
    const filteredAuctions = [];

    for (const auction of allAuctions) {
      // Parse end time
      const endTime = new Date(auction.endTime);

      // Check if auction ends within the time window
      if (endTime > now && endTime <= cutoffTime) {
        // If auction has coordinates, check distance
        if (auction.lat && auction.lon) {
          const distance = calculateDistance(
            targetCoords.lat,
            targetCoords.lon,
            auction.lat,
            auction.lon
          );

          if (distance <= parseInt(radius)) {
            filteredAuctions.push({
              ...auction,
              distance: Math.round(distance * 10) / 10,
              hoursRemaining: Math.round((endTime - now) / (1000 * 60 * 60) * 10) / 10
            });
          }
        } else if (auction.zipCode) {
          // Try to get coordinates for auction ZIP code
          const auctionCoords = await getCoordinatesForZip(auction.zipCode);
          if (auctionCoords) {
            const distance = calculateDistance(
              targetCoords.lat,
              targetCoords.lon,
              auctionCoords.lat,
              auctionCoords.lon
            );

            if (distance <= parseInt(radius)) {
              filteredAuctions.push({
                ...auction,
                lat: auctionCoords.lat,
                lon: auctionCoords.lon,
                distance: Math.round(distance * 10) / 10,
                hoursRemaining: Math.round((endTime - now) / (1000 * 60 * 60) * 10) / 10
              });
            }
          }
        }
      }
    }

    // Sort by distance
    filteredAuctions.sort((a, b) => a.distance - b.distance);

    console.log(`Returning ${filteredAuctions.length} filtered auctions`);

    res.json({
      success: true,
      count: filteredAuctions.length,
      filters: {
        zipCode,
        radius: parseInt(radius),
        hours: parseInt(hours)
      },
      auctions: filteredAuctions
    });

  } catch (error) {
    console.error('Error in /api/auctions:', error);
    res.status(500).json({ error: 'Failed to fetch auctions', message: error.message });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Cleanup on exit
process.on('SIGINT', async () => {
  console.log('\nShutting down gracefully...');
  if (browser) {
    await browser.close();
  }
  process.exit(0);
});

app.listen(PORT, () => {
  console.log(`AuctionNinja API server running on http://localhost:${PORT}`);
  console.log(`Try: http://localhost:${PORT}/api/auctions?zipCode=06870&radius=20&hours=24`);
});
