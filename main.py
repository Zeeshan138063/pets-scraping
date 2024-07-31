import requests
from rich import print
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'ocp-apim-subscription-key': '291a9190a1c6453fb7ae13c799ae5665',
    'origin': 'https://www.petsathome.com',
    'pet-care-platform-search-uid': 'uid=2864304789513:v=16.0:ts=1722466273191:hc=1',
    'priority': 'u=1, i',
    'referer': 'https://www.petsathome.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-pcp-correlation-id': '2aa7a82f-8a13-4f8b-86e3-0c5cadaf6454',
    'x-pcp-correlation-session-id': 'd898f54c-a2c4-4b82-a774-982d06691609',
    'x-pcp-origin': 'web/pcp',
    'x-pcp-principal-correlation-id': 'e8b0f270-c8c0-4ca8-9988-a210925c5eb0',
}

params = {
    'searchTerm': 'dog bed',
    'offset': '0',
    'limit': '40',
    'sortBy': 'best-match',
    'searchType': 'Product',
}

response = requests.get('https://api2.petsathome.com/cs/ecomm/api/v1/search', params=params, headers=headers)
print(response.json()['products'])