import requests
r = requests.get("https://data.cityofnewyork.us/api/views/27vb-augk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/water-use-restrictions-summary-of-15-rcny-chapters-20-and-21/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/water-use-restrictions-summary-of-15-rcny-chapters-20-and-21/data.csv"]
