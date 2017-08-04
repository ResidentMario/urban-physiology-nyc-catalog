import requests
r = requests.get("https://data.cityofnewyork.us/api/views/miqs-rvtb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-median-age-by-borough-2000-2030/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-median-age-by-borough-2000-2030/data.csv"]
