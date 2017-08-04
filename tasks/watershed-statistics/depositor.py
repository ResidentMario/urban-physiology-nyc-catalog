import requests
r = requests.get("https://data.cityofnewyork.us/api/views/z4kf-gt4n/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/watershed-statistics/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/watershed-statistics/data.csv"]
