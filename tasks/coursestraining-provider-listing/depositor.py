import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fgq8-am2v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/coursestraining-provider-listing/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/coursestraining-provider-listing/data.csv"]
