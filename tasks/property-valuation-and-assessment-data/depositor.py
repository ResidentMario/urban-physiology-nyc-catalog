import requests
r = requests.get("https://data.cityofnewyork.us/download/rgy2-tti8/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data/data.zip"]
