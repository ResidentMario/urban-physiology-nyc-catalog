import requests
r = requests.get("https://data.cityofnewyork.us/api/views/c4pu-cif5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-alleged-victims-compared-to-new-york-city-demographics-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-alleged-victims-compared-to-new-york-city-demographics-2005-2009/data.csv"]
