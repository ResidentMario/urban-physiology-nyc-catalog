import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q44u-339y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/commuter-van-vehicles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/commuter-van-vehicles/data.csv"]
