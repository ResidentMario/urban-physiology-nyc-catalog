import requests
r = requests.get("https://data.cityofnewyork.us/api/views/87fx-28ei/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wholesale-markets/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wholesale-markets/data.csv"]
