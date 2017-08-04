import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4s7y-vm5x/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-citywide-distribution/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-2011-class-size-citywide-distribution/data.csv"]
