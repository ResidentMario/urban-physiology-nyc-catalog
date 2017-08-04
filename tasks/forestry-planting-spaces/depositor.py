import requests
r = requests.get("https://data.cityofnewyork.us/api/views/82zj-84is/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-planting-spaces/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-planting-spaces/data.csv"]
