import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ka27-qx5k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-cultural-institutions-group-funding/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-cultural-institutions-group-funding/data.csv"]
