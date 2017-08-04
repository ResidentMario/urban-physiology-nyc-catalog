import requests
r = requests.get("https://data.cityofnewyork.us/api/views/itfs-ms3e/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ap-college-board-2010-school-level-results/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ap-college-board-2010-school-level-results/data.csv"]
