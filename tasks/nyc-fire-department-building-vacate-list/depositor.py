import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n5xc-7jfa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-fire-department-building-vacate-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-fire-department-building-vacate-list/data.csv"]
