import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rmmq-46n5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/food-scrap-drop-off-sites/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/food-scrap-drop-off-sites/data.csv"]
