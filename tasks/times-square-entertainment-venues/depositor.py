import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jxdc-hnze/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-entertainment-venues/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-entertainment-venues/data.csv"]
