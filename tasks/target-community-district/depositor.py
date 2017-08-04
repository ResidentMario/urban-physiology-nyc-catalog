import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tngj-drbu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/target-community-district/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/target-community-district/data.csv"]
