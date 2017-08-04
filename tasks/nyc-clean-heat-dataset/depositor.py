import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8isn-pgv3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-clean-heat-dataset/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-clean-heat-dataset/data.csv"]
