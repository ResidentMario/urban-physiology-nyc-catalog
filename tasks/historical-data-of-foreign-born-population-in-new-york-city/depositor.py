import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8qru-nyj8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-data-of-foreign-born-population-in-new-york-city/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-data-of-foreign-born-population-in-new-york-city/data.csv"]
