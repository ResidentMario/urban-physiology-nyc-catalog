import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sjfe-fppp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers-status-change-log-10282013-present/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers-status-change-log-10282013-present/data.csv"]
