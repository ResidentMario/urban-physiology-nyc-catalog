import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b79y-xcs9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plants/data.csv"]
