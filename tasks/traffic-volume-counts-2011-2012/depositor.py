import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wng2-85mv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/traffic-volume-counts-2011-2012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/traffic-volume-counts-2011-2012/data.csv"]
