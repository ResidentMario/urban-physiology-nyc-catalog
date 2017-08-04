import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vpb3-uf7s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/child-health-plus-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/child-health-plus-income-levels/data.csv"]
