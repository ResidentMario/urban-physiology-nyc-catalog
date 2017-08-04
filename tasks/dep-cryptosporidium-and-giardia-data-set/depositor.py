import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x2s6-6d2j/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-cryptosporidium-and-giardia-data-set/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-cryptosporidium-and-giardia-data-set/data.csv"]
