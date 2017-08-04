import requests
r = requests.get("https://data.cityofnewyork.us/download/39yy-hdfd/application%2Fvnd.ms-excel")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/land-acquisition-statistics/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/land-acquisition-statistics/data.xls"]
