#!/bin/bash

# AuctionNinja App Startup Script

echo "🚀 Starting AuctionNinja Nearby Finder..."
echo ""

# Check if node_modules exists in both directories
if [ ! -d "backend/node_modules" ] || [ ! -d "frontend/node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm run install:all
    echo ""
fi

echo "✅ Starting development servers..."
echo "   Backend:  http://localhost:3001"
echo "   Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop the servers"
echo ""

npm run dev
