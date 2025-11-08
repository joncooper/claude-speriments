import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [auctions, setAuctions] = useState([])
  const [filteredAuctions, setFilteredAuctions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Filter states
  const [zipCode, setZipCode] = useState('06870')
  const [radius, setRadius] = useState(20)
  const [hours, setHours] = useState(24)
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')
  const [sortBy, setSortBy] = useState('distance')

  // Fetch auctions from API
  const fetchAuctions = async () => {
    setLoading(true)
    setError(null)

    try {
      const response = await axios.get('/api/auctions', {
        params: { zipCode, radius, hours }
      })

      if (response.data.success) {
        setAuctions(response.data.auctions)
        setFilteredAuctions(response.data.auctions)
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to fetch auctions')
      console.error('Error fetching auctions:', err)
    } finally {
      setLoading(false)
    }
  }

  // Initial fetch
  useEffect(() => {
    fetchAuctions()
  }, [])

  // Apply filters and sorting
  useEffect(() => {
    let filtered = [...auctions]

    // Filter by search query
    if (searchQuery) {
      filtered = filtered.filter(auction =>
        auction.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        auction.location.toLowerCase().includes(searchQuery.toLowerCase())
      )
    }

    // Filter by category
    if (selectedCategory !== 'all') {
      filtered = filtered.filter(auction => auction.category === selectedCategory)
    }

    // Sort
    filtered.sort((a, b) => {
      switch (sortBy) {
        case 'distance':
          return a.distance - b.distance
        case 'time':
          return a.hoursRemaining - b.hoursRemaining
        case 'items':
          return (b.items || 0) - (a.items || 0)
        default:
          return 0
      }
    })

    setFilteredAuctions(filtered)
  }, [auctions, searchQuery, selectedCategory, sortBy])

  // Get unique categories
  const categories = ['all', ...new Set(auctions.map(a => a.category).filter(Boolean))]

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-xl">🔨</span>
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">AuctionNinja Nearby</h1>
                <p className="text-sm text-gray-600">Find auctions ending soon</p>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Search and Filters */}
        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                ZIP Code
              </label>
              <input
                type="text"
                value={zipCode}
                onChange={(e) => setZipCode(e.target.value)}
                className="input-field w-full"
                placeholder="06870"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Radius (miles)
              </label>
              <input
                type="number"
                value={radius}
                onChange={(e) => setRadius(e.target.value)}
                className="input-field w-full"
                min="1"
                max="100"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Ending Within (hours)
              </label>
              <input
                type="number"
                value={hours}
                onChange={(e) => setHours(e.target.value)}
                className="input-field w-full"
                min="1"
                max="168"
              />
            </div>

            <div className="flex items-end">
              <button
                onClick={fetchAuctions}
                disabled={loading}
                className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'Searching...' : 'Search'}
              </button>
            </div>
          </div>

          {/* Secondary Filters */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-gray-200">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Search
              </label>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="input-field w-full"
                placeholder="Search auctions..."
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Category
              </label>
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="input-field w-full"
              >
                {categories.map(cat => (
                  <option key={cat} value={cat}>
                    {cat.charAt(0).toUpperCase() + cat.slice(1)}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Sort By
              </label>
              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                className="input-field w-full"
              >
                <option value="distance">Distance (nearest)</option>
                <option value="time">Ending Soon</option>
                <option value="items">Most Items</option>
              </select>
            </div>
          </div>
        </div>

        {/* Results Summary */}
        {!loading && !error && (
          <div className="mb-4 flex items-center justify-between">
            <p className="text-gray-600">
              Found <span className="font-semibold text-gray-900">{filteredAuctions.length}</span> auctions
            </p>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <div className="flex items-center">
              <span className="text-red-600 text-xl mr-3">⚠️</span>
              <div>
                <h3 className="text-red-900 font-semibold">Error</h3>
                <p className="text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map(i => (
              <div key={i} className="card animate-pulse">
                <div className="bg-gray-300 h-48 w-full"></div>
                <div className="p-4 space-y-3">
                  <div className="h-6 bg-gray-300 rounded w-3/4"></div>
                  <div className="h-4 bg-gray-300 rounded w-1/2"></div>
                  <div className="h-4 bg-gray-300 rounded w-2/3"></div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Auction Cards */}
        {!loading && !error && filteredAuctions.length === 0 && (
          <div className="text-center py-12">
            <div className="text-6xl mb-4">🔍</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">No auctions found</h3>
            <p className="text-gray-600">
              Try adjusting your search filters or expanding the search radius
            </p>
          </div>
        )}

        {!loading && !error && filteredAuctions.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredAuctions.map(auction => (
              <div key={auction.id} className="card">
                {/* Auction Image */}
                <div className="relative h-48 overflow-hidden bg-gray-200">
                  <img
                    src={auction.image}
                    alt={auction.title}
                    className="w-full h-full object-cover"
                    onError={(e) => {
                      e.target.src = 'https://via.placeholder.com/400x300?text=No+Image'
                    }}
                  />
                  {auction.category && (
                    <div className="absolute top-3 right-3 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-semibold text-gray-700">
                      {auction.category}
                    </div>
                  )}
                </div>

                {/* Auction Details */}
                <div className="p-5">
                  <h3 className="text-lg font-bold text-gray-900 mb-2 line-clamp-2">
                    {auction.title}
                  </h3>

                  <div className="space-y-2 mb-4">
                    {/* Location */}
                    <div className="flex items-start text-sm text-gray-600">
                      <span className="mr-2">📍</span>
                      <span>{auction.location}</span>
                    </div>

                    {/* Distance */}
                    <div className="flex items-center text-sm">
                      <span className="mr-2">🚗</span>
                      <span className="font-semibold text-primary-600">
                        {auction.distance} miles away
                      </span>
                    </div>

                    {/* Time Remaining */}
                    <div className="flex items-center text-sm">
                      <span className="mr-2">⏰</span>
                      <span className={`font-semibold ${
                        auction.hoursRemaining < 6 ? 'text-red-600' :
                        auction.hoursRemaining < 12 ? 'text-orange-600' :
                        'text-green-600'
                      }`}>
                        Ends in {auction.hoursRemaining}h
                      </span>
                    </div>

                    {/* Items Count */}
                    {auction.items && (
                      <div className="flex items-center text-sm text-gray-600">
                        <span className="mr-2">📦</span>
                        <span>{auction.items} items</span>
                      </div>
                    )}
                  </div>

                  {/* Action Button */}
                  <a
                    href={auction.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn-primary w-full text-center inline-block"
                  >
                    View Auction
                  </a>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <p className="text-center text-gray-600 text-sm">
            AuctionNinja Nearby Finder - Find local auctions ending soon
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App
