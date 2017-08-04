import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y43c-5n92/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/watershed-water-quality-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/watershed-water-quality-data/data.csv"]
