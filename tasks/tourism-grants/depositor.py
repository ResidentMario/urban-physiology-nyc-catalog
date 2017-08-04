import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x4ud-jhxu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tourism-grants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tourism-grants/data.csv"]
