# AuctionNinja Nearby Finder - Implementation Notes

## Overview

Built as a full-stack web application to help users find auctions on AuctionNinja.com that are ending soon and located nearby. The application uses headless browser automation to scrape auction data and provides a modern, mobile-responsive interface for browsing and filtering results.

## Architecture Decisions

### Frontend: React + Vite + Tailwind CSS

**Why React?**
- Component-based architecture for reusable UI elements
- Large ecosystem and developer familiarity
- Excellent mobile support with responsive design patterns

**Why Vite?**
- Extremely fast development server with HMR (Hot Module Replacement)
- Optimized production builds
- Modern ES modules support
- Simpler configuration than webpack

**Why Tailwind CSS?**
- Utility-first approach for rapid UI development
- Consistent design system out of the box
- Excellent mobile-first responsive utilities
- Small production bundle size with tree-shaking

### Backend: Node.js + Express + Puppeteer

**Why Puppeteer?**
- AuctionNinja.com likely uses JavaScript for dynamic content
- Headless Chrome can bypass basic bot detection
- Can handle any JavaScript-rendered content
- More reliable than simple HTTP requests + HTML parsing

**Why Express?**
- Minimal, flexible web framework
- Easy to set up RESTful API endpoints
- Large middleware ecosystem
- Perfect for this small API surface

**Alternative Considered: Axios + Cheerio**
- Initially tried this approach but got 403 errors
- Couldn't handle JavaScript-rendered content
- Puppeteer was the necessary upgrade

### Data Flow

1. **User makes search request** from frontend (ZIP code, radius, hours)
2. **Frontend calls backend API** via `/api/auctions` endpoint
3. **Backend checks cache** (5-minute TTL to reduce load)
4. **If not cached, Puppeteer scrapes** AuctionNinja.com
5. **Backend geocodes ZIP codes** using free zippopotam.us API
6. **Backend filters by distance** using Haversine formula
7. **Backend filters by time** based on auction end times
8. **Backend returns filtered results** to frontend
9. **Frontend displays** with sorting, filtering, search

## Key Implementation Details

### Web Scraping Strategy

The scraper uses an **adaptive selector approach**:

```javascript
const possibleSelectors = [
  'article',
  '[class*="auction"]',
  '[class*="listing"]',
  '[class*="item"]',
  '.card',
  '[class*="card"]'
];
```

This tries multiple selector patterns to find auction listings, making it more resilient to HTML structure changes.

### Time Parsing

Handles multiple time formats:
- Relative times: "Ends in 3 hours", "2h 30m", "1d 5h"
- Absolute dates: ISO strings, standard date formats
- Graceful fallback to 12 hours if parsing fails

### Distance Calculation

Uses the **Haversine formula** for accurate distance calculation:
- Accounts for Earth's curvature
- Returns distance in miles
- Accuracy within ~0.5% for most distances

### Caching Strategy

- **5-minute cache** on auction data reduces server load
- Browser instance reuse prevents repeated Chromium launches
- ZIP code coordinates could be cached longer (rarely change)

### Error Handling

- Falls back to mock data if scraping fails
- Graceful degradation at every level
- Clear console logging for debugging
- User-friendly error messages in UI

## Development Environment

### Node.js Version
- Requires Node.js 18+ for native fetch API
- ES modules throughout (type: "module")

### Browser Dependencies (Puppeteer)
- Downloads Chromium (~150MB) on first install
- May require system dependencies on Linux
- Headless mode for production

## Performance Considerations

### Frontend
- Lazy loading could be added for large result sets
- Image loading is already lazy (browser default)
- Tailwind CSS purged in production

### Backend
- Browser instance reuse is critical for performance
- Caching prevents repeated scraping
- Could add request queuing for high traffic

### Scalability Bottlenecks
- Single browser instance limits concurrent scraping
- Could use browser pool for production
- Rate limiting recommended for AuctionNinja.com

## Security Considerations

- CORS enabled (currently allow all origins)
- No authentication/authorization (public API)
- Input validation on ZIP codes
- Sandboxed Puppeteer with security flags

For production:
- Add rate limiting
- Implement proper CORS configuration
- Add request validation/sanitization
- Consider API authentication

## Testing Strategy

### Current Testing
- Manual testing during development
- Mock data for UI development
- Console logging for debugging

### Future Testing
- Unit tests for distance calculation
- Integration tests for API endpoints
- E2E tests for scraping logic
- Visual regression tests for UI

## Deployment Considerations

### Frontend Deployment
- `npm run build` creates optimized production build
- Static files in `frontend/dist/`
- Can deploy to Vercel, Netlify, or any static host

### Backend Deployment
- Requires Node.js runtime
- Puppeteer requires Chrome/Chromium
- Consider serverless with Chrome layer (AWS Lambda, etc.)
- Or traditional VPS/container deployment

### Environment Variables
Currently none required, but should add:
- `PORT` for backend
- `API_URL` for frontend
- `CACHE_TTL` for cache duration
- `NODE_ENV` for environment detection

## Known Limitations

1. **Scraping depends on HTML structure** - May break if AuctionNinja changes their markup
2. **No real-time updates** - Data cached for 5 minutes
3. **Limited error recovery** - Falls back to mock data rather than retrying
4. **No user accounts** - Can't save searches or get notifications
5. **Single ZIP code search** - Can't search multiple locations simultaneously

## Lessons Learned

1. **Start with simplest approach** - Tried Axios first, upgraded to Puppeteer when needed
2. **Adaptive selectors are key** - Website structure may vary
3. **Graceful degradation matters** - Mock data allows development without working scraper
4. **Caching is essential** - Reduces load and improves UX
5. **Mobile-first design** - Tailwind's mobile utilities make responsive design easy

## Future Improvements

See [ICEBOX.md](./ICEBOX.md) for detailed feature ideas.

---

**Last Updated:** November 2025
