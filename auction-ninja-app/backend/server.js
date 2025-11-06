import express from 'express';
import cors from 'cors';
import axios from 'axios';
import * as cheerio from 'cheerio';
import NodeCache from 'node-cache';

const app = express();
const PORT = 3001;

// Cache auction data for 5 minutes
const cache = new NodeCache({ stdTTL: 300 });

app.use(cors());
app.use(express.json());

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
    // Using a free geocoding service
    const response = await axios.get(`https://api.zippopotam.us/us/${zipCode}`);
    if (response.data && response.data.places && response.data.places[0]) {
      return {
        lat: parseFloat(response.data.places[0].latitude),
        lon: parseFloat(response.data.places[0].longitude)
      };
    }
  } catch (error) {
    console.error('Error fetching coordinates for ZIP:', error.message);
  }
  return null;
}

// Helper function to parse auction end time
function parseAuctionEndTime(timeString) {
  try {
    // This will need to be adjusted based on actual AuctionNinja format
    // For now, we'll handle common formats
    const date = new Date(timeString);
    return date;
  } catch (error) {
    console.error('Error parsing time:', error);
    return null;
  }
}

// Fetch auctions from AuctionNinja
async function fetchAuctionNinjaData() {
  const cachedData = cache.get('auctions');
  if (cachedData) {
    console.log('Returning cached auction data');
    return cachedData;
  }

  try {
    console.log('Fetching fresh auction data...');

    // Try to fetch the auctions page with proper headers
    const response = await axios.get('https://www.auctionninja.com/auctions', {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
      },
      timeout: 10000
    });

    const $ = cheerio.load(response.data);
    const auctions = [];

    // This selector will need to be adjusted based on actual HTML structure
    // We'll need to inspect the page to get the right selectors
    $('.auction-item, .auction-card, [class*="auction"]').each((i, elem) => {
      const $elem = $(elem);

      // Extract auction details - these selectors are placeholders
      const title = $elem.find('.title, .auction-title, h2, h3').first().text().trim();
      const location = $elem.find('.location, .auction-location, [class*="location"]').first().text().trim();
      const endTime = $elem.find('.end-time, .closing-time, [class*="time"]').first().text().trim();
      const link = $elem.find('a').first().attr('href');
      const image = $elem.find('img').first().attr('src');

      if (title) {
        auctions.push({
          id: i,
          title,
          location,
          endTime,
          link: link ? (link.startsWith('http') ? link : `https://www.auctionninja.com${link}`) : '',
          image: image ? (image.startsWith('http') ? image : `https://www.auctionninja.com${image}`) : '',
          rawHtml: $elem.html() // Keep raw HTML for debugging
        });
      }
    });

    console.log(`Found ${auctions.length} auctions`);

    if (auctions.length > 0) {
      cache.set('auctions', auctions);
      return auctions;
    }

    // If no auctions found, return mock data for testing
    console.log('No auctions found, returning mock data for development');
    return getMockAuctions();

  } catch (error) {
    console.error('Error fetching auction data:', error.message);
    // Return mock data if fetching fails
    return getMockAuctions();
  }
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

app.listen(PORT, () => {
  console.log(`AuctionNinja API server running on http://localhost:${PORT}`);
  console.log(`Try: http://localhost:${PORT}/api/auctions?zipCode=06870&radius=20&hours=24`);
});
