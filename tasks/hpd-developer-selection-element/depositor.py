import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fged-sxa8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-developer-selection-element/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-developer-selection-element/data.csv"]
