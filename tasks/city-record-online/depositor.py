import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dg92-zbpx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-record-online/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-record-online/data.csv"]
