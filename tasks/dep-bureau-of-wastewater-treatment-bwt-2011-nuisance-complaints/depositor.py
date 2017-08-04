import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qiku-f5v3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-bureau-of-wastewater-treatment-bwt-2011-nuisance-complaints/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-bureau-of-wastewater-treatment-bwt-2011-nuisance-complaints/data.csv"]
