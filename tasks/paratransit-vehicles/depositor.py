import requests
r = requests.get("https://data.cityofnewyork.us/api/views/v39y-4v3t/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/paratransit-vehicles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/paratransit-vehicles/data.csv"]
