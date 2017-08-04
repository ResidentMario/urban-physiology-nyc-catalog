import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8qgy-ka3v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdep-recreation-area-maps/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdep-recreation-area-maps/data.csv"]
