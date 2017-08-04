import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ck4n-5h6x/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/complaint-log/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/complaint-log/data.csv"]
