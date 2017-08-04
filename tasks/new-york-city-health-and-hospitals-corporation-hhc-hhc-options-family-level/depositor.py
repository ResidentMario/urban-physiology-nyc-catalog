import requests
r = requests.get("https://data.cityofnewyork.us/api/views/32yu-maz2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-health-and-hospitals-corporation-hhc-hhc-options-family-level/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-health-and-hospitals-corporation-hhc-hhc-options-family-level/data.csv"]
