import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uedp-fegm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/natural-gas-consumption-by-zip-code-2010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/natural-gas-consumption-by-zip-code-2010/data.csv"]
