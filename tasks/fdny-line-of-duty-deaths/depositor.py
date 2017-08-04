import requests
r = requests.get("https://data.cityofnewyork.us/api/views/32y8-s55c/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-line-of-duty-deaths/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-line-of-duty-deaths/data.csv"]
