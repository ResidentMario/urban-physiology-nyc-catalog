import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jqy3-ybjq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/council-district-breakdown/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/council-district-breakdown/data.csv"]
