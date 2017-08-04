import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8r6c-ydwk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/monthly-indicators/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/monthly-indicators/data.csv"]
