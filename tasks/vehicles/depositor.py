import requests
r = requests.get("https://data.cityofnewyork.us/api/views/28rh-vpvr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/vehicles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/vehicles/data.csv"]
