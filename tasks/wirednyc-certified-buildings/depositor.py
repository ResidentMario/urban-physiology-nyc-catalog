import requests
r = requests.get("https://data.cityofnewyork.us/api/views/37it-gmcp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-certified-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-certified-buildings/data.csv"]
