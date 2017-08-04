import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q39e-7gbs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/energy-and-water-data-disclosure-for-local-law-84-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/energy-and-water-data-disclosure-for-local-law-84-2011/data.csv"]
