import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a6zp-tcs3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy-2017-pmmr-data-extract/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy-2017-pmmr-data-extract/data.csv"]
