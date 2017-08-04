import requests
r = requests.get("https://data.cityofnewyork.us/api/views/h5nh-eqde/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/columbus-avenue-bid-businesses/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/columbus-avenue-bid-businesses/data.csv"]
