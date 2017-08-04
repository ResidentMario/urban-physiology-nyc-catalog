import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ghpb-fpea/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2013-green-taxi-trip-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2013-green-taxi-trip-data/data.csv"]
