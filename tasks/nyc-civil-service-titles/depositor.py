import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nzjr-3966/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-civil-service-titles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-civil-service-titles/data.csv"]
