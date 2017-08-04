import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s4kf-3yrf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-locations/data.csv"]
