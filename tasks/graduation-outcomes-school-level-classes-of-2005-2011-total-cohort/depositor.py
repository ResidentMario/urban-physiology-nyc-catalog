import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cma4-zi8m/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-of-2005-2011-total-cohort/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-of-2005-2011-total-cohort/data.csv"]
