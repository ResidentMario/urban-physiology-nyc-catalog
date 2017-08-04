import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jr3e-jwne/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hero-banner/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hero-banner/data.csv"]
