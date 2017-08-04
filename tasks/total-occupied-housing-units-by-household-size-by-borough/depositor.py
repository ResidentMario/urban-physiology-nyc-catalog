import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fmzx-suji/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-occupied-housing-units-by-household-size-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-occupied-housing-units-by-household-size-by-borough/data.csv"]
