import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8ius-dhrr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-tract-to-neighborhood-tabulation-area-equivalency-table/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-tract-to-neighborhood-tabulation-area-equivalency-table/data.csv"]
