import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hvrh-b6nb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-green-taxi-trip-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-green-taxi-trip-data/data.csv"]
