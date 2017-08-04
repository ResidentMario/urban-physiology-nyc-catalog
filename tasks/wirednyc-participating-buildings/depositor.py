import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cfzn-4iza/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-participating-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-participating-buildings/data.csv"]
