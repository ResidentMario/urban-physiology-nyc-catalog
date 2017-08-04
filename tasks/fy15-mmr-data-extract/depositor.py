import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xn73-3kak/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy15-mmr-data-extract/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy15-mmr-data-extract/data.csv"]
