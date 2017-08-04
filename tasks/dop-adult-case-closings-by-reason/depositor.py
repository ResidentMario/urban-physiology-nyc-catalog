import requests
r = requests.get("https://data.cityofnewyork.us/api/views/u6p4-fsey/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-case-closings-by-reason/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-case-closings-by-reason/data.csv"]
