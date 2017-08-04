import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hcv4-fhfs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2007/data.csv"]
