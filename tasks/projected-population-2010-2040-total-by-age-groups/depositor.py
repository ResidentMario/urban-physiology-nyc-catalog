import requests
r = requests.get("https://data.cityofnewyork.us/api/views/97pn-acdf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-total-by-age-groups/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-total-by-age-groups/data.csv"]
