import requests
r = requests.get("https://data.cityofnewyork.us/api/views/97zg-4p9t/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/applications-tracking-table/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/applications-tracking-table/data.csv"]
