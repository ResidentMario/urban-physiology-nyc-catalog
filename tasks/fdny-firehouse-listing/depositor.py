import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hc8x-tcnd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-firehouse-listing/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-firehouse-listing/data.csv"]
