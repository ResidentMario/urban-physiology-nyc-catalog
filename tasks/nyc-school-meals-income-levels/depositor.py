import requests
r = requests.get("https://data.cityofnewyork.us/api/views/h7mf-hrsw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-meals-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-meals-income-levels/data.csv"]
