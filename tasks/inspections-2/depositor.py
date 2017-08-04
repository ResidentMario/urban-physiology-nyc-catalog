import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jzhd-m6uv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inspections-2/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inspections-2/data.csv"]
