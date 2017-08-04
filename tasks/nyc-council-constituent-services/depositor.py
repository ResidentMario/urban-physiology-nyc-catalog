import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b9km-gdpy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-council-constituent-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-council-constituent-services/data.csv"]
