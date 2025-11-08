# SEC Data Files

This directory contains SEC financial data gathered via MCP tools.
Files are created automatically during analysis.

## File Format

Files are named: `{TICKER}_sec_data.json`

Example: `AAPL_sec_data.json`

## Structure

Each file contains:
```json
{
  "company_info": {
    "name": "Company Name",
    "cik": "0000000000",
    "ticker": "TICK",
    "sic": "1234",
    "sicDescription": "Industry Description"
  },
  "annual_data": [
    {
      "fiscal_year_end": "2023-12-31",
      "form": "10-K",
      "Revenues": 1000000,
      "CostOfRevenue": 500000,
      "Assets": 5000000,
      ...
    }
  ]
}
```

## Data Source

Data is gathered using SEC EDGAR MCP tools, which fetch information directly from
the SEC's official EDGAR database.
