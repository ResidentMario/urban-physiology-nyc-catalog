import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9m35-jch2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-openrecords-foil-request-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-openrecords-foil-request-data/data.csv"]
