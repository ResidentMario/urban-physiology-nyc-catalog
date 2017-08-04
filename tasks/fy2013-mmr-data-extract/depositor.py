import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6xp4-c9qp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy2013-mmr-data-extract/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy2013-mmr-data-extract/data.csv"]
