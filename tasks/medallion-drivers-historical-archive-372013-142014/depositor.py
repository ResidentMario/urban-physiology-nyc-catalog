import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n776-dsqy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers-historical-archive-372013-142014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers-historical-archive-372013-142014/data.csv"]
