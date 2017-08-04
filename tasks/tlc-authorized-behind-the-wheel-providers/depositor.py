import requests
r = requests.get("https://data.cityofnewyork.us/api/views/auuc-fqzi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-authorized-behind-the-wheel-providers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-authorized-behind-the-wheel-providers/data.csv"]
