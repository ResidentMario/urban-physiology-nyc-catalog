import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sxx4-xhzg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-recycling-bins/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-recycling-bins/data.csv"]
