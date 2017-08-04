import requests
r = requests.get("http://citibikenyc.com/stations/json")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citi-bike-live-station-feed-json/data.json", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citi-bike-live-station-feed-json/data.json"]
