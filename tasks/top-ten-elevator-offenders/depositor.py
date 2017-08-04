import requests
r = requests.get("https://data.cityofnewyork.us/api/views/u3bu-v2bf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/top-ten-elevator-offenders/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/top-ten-elevator-offenders/data.csv"]
