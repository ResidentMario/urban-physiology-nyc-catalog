import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vg63-xw6u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-expenditures/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-expenditures/data.csv"]
