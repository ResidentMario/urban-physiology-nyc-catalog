import requests
r = requests.get("https://data.cityofnewyork.us/api/views/khqi-x3p3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-of-2005-2011-gender/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-school-level-classes-of-2005-2011-gender/data.csv"]
