import requests
r = requests.get("https://data.cityofnewyork.us/api/views/473p-afgy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plant-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plant-data/data.csv"]
