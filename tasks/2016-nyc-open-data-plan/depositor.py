import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vdem-2i66/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-nyc-open-data-plan/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-nyc-open-data-plan/data.csv"]
