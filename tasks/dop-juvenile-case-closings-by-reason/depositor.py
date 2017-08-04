import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wha7-46h5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-closings-by-reason/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-closings-by-reason/data.csv"]
