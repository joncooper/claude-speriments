# AuctionNinja Nearby Finder

A modern, responsive web application that helps you find auctions on AuctionNinja.com that are ending soon and located near you.

## Features

- 🎯 **Location-based filtering** - Find auctions within a specific radius of any ZIP code
- ⏰ **Time-based filtering** - Show only auctions ending within a specified time window
- 🔍 **Advanced search** - Search by title, location, and category
- 📱 **Mobile-responsive** - Beautiful UI that works perfectly on mobile and desktop
- 🎨 **Modern design** - Sleek, professional interface built with Tailwind CSS
- 📊 **Multiple sorting options** - Sort by distance, time remaining, or item count

## Technology Stack

### Frontend
- React 18
- Vite (for fast development and optimized builds)
- Tailwind CSS (for beautiful, responsive styling)
- Axios (for API requests)

### Backend
- Node.js with Express
- Cheerio (for web scraping)
- Node-cache (for performance optimization)
- Axios (for HTTP requests)

## Quick Start

### Prerequisites
- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. Install all dependencies:
```bash
npm run install:all
```

2. Start the development servers:
```bash
npm run dev
```

This will start:
- Backend API on http://localhost:3001
- Frontend app on http://localhost:3000

### Manual Setup

If you prefer to set up manually:

1. Install backend dependencies:
```bash
cd backend
npm install
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Start the backend server:
```bash
cd backend
npm run dev
```

4. In a new terminal, start the frontend:
```bash
cd frontend
npm run dev
```

## Usage

1. Open http://localhost:3000 in your browser
2. Enter your ZIP code (default: 06870)
3. Set your search radius in miles (default: 20 miles)
4. Set the time window in hours (default: 24 hours)
5. Click "Search" to find auctions
6. Use additional filters to refine your results:
   - Search by keyword
   - Filter by category
   - Sort by distance, time, or item count

## API Endpoints

### GET /api/auctions
Fetch auctions based on filters.

**Query Parameters:**
- `zipCode` (string) - ZIP code to search near (default: "06870")
- `radius` (number) - Search radius in miles (default: 20)
- `hours` (number) - Time window in hours (default: 24)

**Example:**
```bash
curl "http://localhost:3001/api/auctions?zipCode=06870&radius=20&hours=24"
```

### GET /api/health
Health check endpoint.

## Project Structure

```
auction-ninja-app/
├── backend/
│   ├── server.js          # Express server with scraping logic
│   └── package.json       # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── main.jsx       # React entry point
│   │   └── index.css      # Tailwind styles
│   ├── index.html         # HTML entry point
│   ├── vite.config.js     # Vite configuration
│   ├── tailwind.config.js # Tailwind configuration
│   └── package.json       # Frontend dependencies
├── package.json           # Root package.json for easy setup
└── README.md              # This file
```

## Features in Detail

### Location Filtering
Uses the Haversine formula to calculate accurate distances between the search location and auction locations. Auctions are sorted by distance by default.

### Time Filtering
Filters auctions based on their end time, showing only those ending within your specified time window. Visual indicators show urgency:
- 🔴 Red: Ends in less than 6 hours
- 🟠 Orange: Ends in 6-12 hours
- 🟢 Green: Ends in 12+ hours

### Search and Categories
- Full-text search across auction titles and locations
- Category filtering (automatically detected from auction data)
- Multiple sorting options for optimal browsing

### Mobile Optimization
- Fully responsive layout
- Touch-friendly interface
- Optimized for various screen sizes
- Fast loading times

## Development

### Backend Development
The backend uses Node.js watch mode for automatic reloading:
```bash
cd backend
npm run dev
```

### Frontend Development
Vite provides hot module replacement for instant updates:
```bash
cd frontend
npm run dev
```

## Production Build

Build the frontend for production:
```bash
cd frontend
npm run build
```

The optimized build will be in `frontend/dist/`.

## Notes

- The application includes mock data for development/testing when AuctionNinja.com is not accessible
- Auction data is cached for 5 minutes to improve performance
- The scraper respects rate limits and includes proper headers

## Troubleshooting

### Port already in use
If ports 3000 or 3001 are already in use, you can change them:
- Frontend: Edit `frontend/vite.config.js`
- Backend: Edit `PORT` constant in `backend/server.js`

### No auctions found
- Try increasing the search radius
- Extend the time window (e.g., 48 or 72 hours)
- Check if the ZIP code is valid
- The app includes mock data for testing if real data is unavailable

## Future Enhancements

- User authentication and saved searches
- Email/SMS notifications for new auctions
- Favorite auctions feature
- Map view of auction locations
- Integration with more auction platforms

## License

MIT
