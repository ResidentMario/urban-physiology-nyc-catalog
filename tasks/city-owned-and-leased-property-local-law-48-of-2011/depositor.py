import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4e2n-s75z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-local-law-48-of-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-local-law-48-of-2011/data.csv"]
