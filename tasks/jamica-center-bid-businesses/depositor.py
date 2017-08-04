import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x84u-rirx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/jamica-center-bid-businesses/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/jamica-center-bid-businesses/data.csv"]
