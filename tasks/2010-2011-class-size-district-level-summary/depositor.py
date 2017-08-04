import requests
r = requests.get("https://data.cityofnewyork.us/api/views/82rt-zc4y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-district-level-summary/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-district-level-summary/data.csv"]
