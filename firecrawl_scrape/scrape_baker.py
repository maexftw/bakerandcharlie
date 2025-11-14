import requests
import json

url = "https://api.firecrawl.dev/v2/scrape"

payload = {
    "url": "https://baker-v2-bfe158.webflow.io/",
    "onlyMainContent": False,
    "maxAge": 172800000,
    "parsers": [
        "pdf"
    ],
    "formats": [
        "markdown"
    ]
}

headers = {
    "Authorization": "Bearer fc-d21288c226fd43bba3a8ca4418996218",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

# Print the response
print(json.dumps(response.json(), indent=2))

# Save the response to a file
with open('scrape_result.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, indent=2, ensure_ascii=False)

print("\n\nResult saved to scrape_result.json")
