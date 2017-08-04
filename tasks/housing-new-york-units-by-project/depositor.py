import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hq68-rnsi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-new-york-units-by-project/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-new-york-units-by-project/data.csv"]
