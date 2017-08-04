import requests
r = requests.get("https://data.cityofnewyork.us/api/views/azxq-2skx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-rent-affordability-element/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-rent-affordability-element/data.csv"]
