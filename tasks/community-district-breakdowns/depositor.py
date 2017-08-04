import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w3c6-35wg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-district-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-district-breakdowns/data.csv"]
