import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8gqz-6v9v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/downtown-brooklyn-partnership-dbp-court-livingston-schermerhorn-cls-retail-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/downtown-brooklyn-partnership-dbp-court-livingston-schermerhorn-cls-retail-locations/data.csv"]
