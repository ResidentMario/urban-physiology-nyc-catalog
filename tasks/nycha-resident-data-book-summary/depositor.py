import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5r5y-pvs3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-resident-data-book-summary/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-resident-data-book-summary/data.csv"]
