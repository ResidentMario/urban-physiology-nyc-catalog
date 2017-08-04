import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5jwd-xj5z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/preferred-source-procurements-fy15/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/preferred-source-procurements-fy15/data.csv"]
