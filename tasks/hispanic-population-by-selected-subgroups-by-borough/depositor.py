import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w9du-8cu6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hispanic-population-by-selected-subgroups-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hispanic-population-by-selected-subgroups-by-borough/data.csv"]
