import requests
r = requests.get("https://data.cityofnewyork.us/api/views/733r-da8r/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cultural-institutions-by-block-and-lot/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cultural-institutions-by-block-and-lot/data.csv"]
