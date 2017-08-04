import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6pwv-zmgh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicles-lpep-provider/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicles-lpep-provider/data.csv"]
