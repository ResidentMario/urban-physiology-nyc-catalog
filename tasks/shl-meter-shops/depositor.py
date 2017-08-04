import requests
r = requests.get("https://data.cityofnewyork.us/api/views/56e3-rp8d/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-meter-shops/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-meter-shops/data.csv"]
