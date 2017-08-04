import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ph5g-sr3v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-summary/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-summary/data.csv"]
