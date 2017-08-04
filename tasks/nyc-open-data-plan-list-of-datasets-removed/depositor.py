import requests
r = requests.get("https://data.cityofnewyork.us/api/views/unw7-yyit/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-plan-list-of-datasets-removed/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-plan-list-of-datasets-removed/data.csv"]
