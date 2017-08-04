import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uv67-wxba/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/senate-district-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/senate-district-breakdowns/data.csv"]
