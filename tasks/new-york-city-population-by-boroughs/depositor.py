import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9mhd-na2n/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-population-by-boroughs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-population-by-boroughs/data.csv"]
