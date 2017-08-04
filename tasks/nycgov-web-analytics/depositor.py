import requests
r = requests.get("https://data.cityofnewyork.us/api/views/d5zb-ragj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycgov-web-analytics/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycgov-web-analytics/data.csv"]
