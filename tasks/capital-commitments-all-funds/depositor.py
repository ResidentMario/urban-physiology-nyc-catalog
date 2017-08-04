import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8fnh-fcum/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-all-funds/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-all-funds/data.csv"]
