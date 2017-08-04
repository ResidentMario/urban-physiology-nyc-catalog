import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2np7-5jsg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2014-green-taxi-trip-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2014-green-taxi-trip-data/data.csv"]
