import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k8hv-56d7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-class-of-2010-regents-based-math-ela-apm-school-level/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-class-of-2010-regents-based-math-ela-apm-school-level/data.csv"]
