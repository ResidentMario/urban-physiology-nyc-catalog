import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nc67-uf89/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-parking-and-camera-violations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-parking-and-camera-violations/data.csv"]
