import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9i2s-e6hd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ten-year-capital-strategy/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ten-year-capital-strategy/data.csv"]
