import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pd5h-92mc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ged-plus-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ged-plus-locations/data.csv"]
