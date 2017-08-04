import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ruce-cnp6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-fy-2015-data-extract/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-fy-2015-data-extract/data.csv"]
