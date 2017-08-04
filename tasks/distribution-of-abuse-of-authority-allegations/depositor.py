import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bfiu-cc7d/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-of-abuse-of-authority-allegations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-of-abuse-of-authority-allegations/data.csv"]
