import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ym2h-u9dt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/brooklyn-public-library-catalog/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/brooklyn-public-library-catalog/data.csv"]
