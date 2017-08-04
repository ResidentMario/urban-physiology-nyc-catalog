import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vr8p-8shw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/derelict-vehicle-dispositions-tow/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/derelict-vehicle-dispositions-tow/data.csv"]
