import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2j8u-wtju/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/benefits-and-programs-api/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/benefits-and-programs-api/data.csv"]
