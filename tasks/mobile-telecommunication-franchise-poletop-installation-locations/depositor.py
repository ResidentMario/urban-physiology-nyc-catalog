import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tbgj-tdd6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mobile-telecommunication-franchise-poletop-installation-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mobile-telecommunication-franchise-poletop-installation-locations/data.csv"]
