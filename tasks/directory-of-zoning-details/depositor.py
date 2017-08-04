import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fbsa-93dh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-zoning-details/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-zoning-details/data.csv"]
