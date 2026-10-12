import json
from urllib.request import urlopen

url = "https://transport.integration.sl.se/v1/sites?expand=true"
station_name = "solna"

with urlopen(url) as response:
    sites = json.load(response)

for site in sites:
    if station_name in site["name"].lower():
        print(json.dumps(site, indent=2, ensure_ascii=False))