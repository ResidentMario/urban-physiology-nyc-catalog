import requests
r = requests.get("https://data.cityofnewyork.us/api/views/p2q7-at72/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-purchasing-fy15-construction/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-purchasing-fy15-construction/data.csv"]
