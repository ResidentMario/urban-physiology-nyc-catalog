import requests
r = requests.get("https://data.cityofnewyork.us/api/views/48pb-zy2g/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nyc-cable-providers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nyc-cable-providers/data.csv"]
