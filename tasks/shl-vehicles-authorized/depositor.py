import requests
r = requests.get("https://data.cityofnewyork.us/api/views/btfj-je3i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicles-authorized/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicles-authorized/data.csv"]
