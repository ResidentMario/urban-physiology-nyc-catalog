import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yini-w76t/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-for-hire-vehicle-trip-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-for-hire-vehicle-trip-data/data.csv"]
