import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7fnf-kyf4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2005/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-summary-of-neighborhood-sales-in-queens-for-class-1-2-and-3-family-homes-2005/data.csv"]
