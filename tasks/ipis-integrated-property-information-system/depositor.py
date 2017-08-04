import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n5mv-nfpy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ipis-integrated-property-information-system/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ipis-integrated-property-information-system/data.csv"]
