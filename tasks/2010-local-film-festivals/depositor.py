import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yggg-xf4b/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-local-film-festivals/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-local-film-festivals/data.csv"]
