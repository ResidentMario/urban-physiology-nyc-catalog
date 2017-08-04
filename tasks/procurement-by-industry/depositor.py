import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nd82-bi9f/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurement-by-industry/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurement-by-industry/data.csv"]
