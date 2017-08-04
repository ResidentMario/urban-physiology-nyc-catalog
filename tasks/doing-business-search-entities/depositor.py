import requests
r = requests.get("https://data.cityofnewyork.us/api/views/72mk-a8z7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doing-business-search-entities/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doing-business-search-entities/data.csv"]
