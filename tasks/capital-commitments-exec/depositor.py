import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tiex-dv5v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-exec/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-exec/data.csv"]
