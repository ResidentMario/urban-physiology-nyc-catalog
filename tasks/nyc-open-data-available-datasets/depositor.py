import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fwt3-keqw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-available-datasets/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-available-datasets/data.csv"]
