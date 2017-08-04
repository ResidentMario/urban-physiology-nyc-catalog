import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jt7v-77mi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-violations-issued-fiscal-year-2014-august-2013-june-2014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-violations-issued-fiscal-year-2014-august-2013-june-2014/data.csv"]
