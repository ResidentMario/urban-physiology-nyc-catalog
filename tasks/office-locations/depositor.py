import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hkud-vzzj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/office-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/office-locations/data.csv"]
