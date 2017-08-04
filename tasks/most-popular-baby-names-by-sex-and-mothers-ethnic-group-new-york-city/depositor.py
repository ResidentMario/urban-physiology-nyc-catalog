import requests
r = requests.get("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/most-popular-baby-names-by-sex-and-mothers-ethnic-group-new-york-city/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/most-popular-baby-names-by-sex-and-mothers-ethnic-group-new-york-city/data.csv"]
