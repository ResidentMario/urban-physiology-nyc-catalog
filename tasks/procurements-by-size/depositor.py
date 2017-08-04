import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ewmy-2fww/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurements-by-size/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurements-by-size/data.csv"]
