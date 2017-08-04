import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4fnu-iufz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-raw-data-fy-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-raw-data-fy-2013/data.csv"]
