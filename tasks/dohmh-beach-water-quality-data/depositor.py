import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2xir-kwzz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dohmh-beach-water-quality-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dohmh-beach-water-quality-data/data.csv"]
