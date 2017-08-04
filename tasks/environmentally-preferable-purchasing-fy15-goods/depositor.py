import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jt9i-9gxr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-purchasing-fy15-goods/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-purchasing-fy15-goods/data.csv"]
