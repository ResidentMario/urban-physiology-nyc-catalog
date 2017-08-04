import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rubn-abch/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-bureau-of-wastewater-treatment-bwt-2010-nuisance-complaints/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-bureau-of-wastewater-treatment-bwt-2010-nuisance-complaints/data.csv"]
