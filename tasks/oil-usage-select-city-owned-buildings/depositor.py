import requests
r = requests.get("https://data.cityofnewyork.us/api/views/whux-iuiu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oil-usage-select-city-owned-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oil-usage-select-city-owned-buildings/data.csv"]
