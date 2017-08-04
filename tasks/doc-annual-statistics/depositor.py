import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wkaa-8g8b/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doc-annual-statistics/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doc-annual-statistics/data.csv"]
