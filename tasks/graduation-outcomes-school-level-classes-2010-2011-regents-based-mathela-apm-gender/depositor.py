import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qrz6-23fw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-gender/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-gender/data.csv"]
