#!/usr/local/bin/python3
import requests

URL = "https://scanner.tradingview.com/brazil/scan"
params = {
    "filter": [
        {
            "left": "volume",
            "operation": "nempty"
        }
    ],
    "options": {
        "active_symbols_only": True,
        "lang": "pt"
    },
    "symbols": {
        "query": {
            "types": []
        },
        "tickers": []
    },
    "columns": [
        "name",
        "close",
        "change",
        "change_abs",
        "Recommend.All",
        "volume",
        "market_cap_basic",
        "price_earnings_ttm",
        "earnings_per_share_basic_ttm",
        "number_of_employees",
        "sector",
        "description",
        "name",
        "type",
        "subtype",
        "update_mode",
        "pricescale",
        "minmov",
        "fractional",
        "minmove2",
        "market_cap_basic",
        "change|1",
        "change|5",
        "change|15",
        "change|60",
        "change|240",
        "change",
        "Perf.W",
        "Perf.1M",
        "Perf.3M",
        "Perf.6M",
        "Perf.YTD",
        "Perf.Y",
        "beta_1_year",
        "Volatility.D"
    ],
    "sort": {
        "sortBy": "volume",
        "sortOrder": "desc"
    },
    "range": [
        0,
        1
    ]
}
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.16.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "34590594-db19-44c5-a94e-fd4fc6de4801,d746f0bc-9479-43d4-a63d-9fcef8db08de",
    'Host': "scanner.tradingview.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "1189",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
response = requests.get(URL, params)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
data = response.json()
print(data)
