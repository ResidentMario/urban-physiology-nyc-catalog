import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ujdf-5byz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/funded-capacity-seats-and-additional-needs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/funded-capacity-seats-and-additional-needs/data.csv"]
