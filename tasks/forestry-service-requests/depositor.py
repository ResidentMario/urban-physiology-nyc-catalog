import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mu46-p9is/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-service-requests/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-service-requests/data.csv"]
