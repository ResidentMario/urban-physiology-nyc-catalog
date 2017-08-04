import requests
r = requests.get("https://data.cityofnewyork.us/api/views/i6as-kc83/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-total-cohort/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-2010-2011-regents-based-mathela-apm-total-cohort/data.csv"]
