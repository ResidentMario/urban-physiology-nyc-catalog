import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mgjt-zuui/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/damage-by-sandy-by-age-of-building/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/damage-by-sandy-by-age-of-building/data.csv"]
