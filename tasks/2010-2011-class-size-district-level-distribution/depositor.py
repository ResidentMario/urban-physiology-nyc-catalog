import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nurr-mhyi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-district-level-distribution/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-district-level-distribution/data.csv"]
