import requests
r = requests.get("https://data.cityofnewyork.us/api/views/avir-tzek/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-classes-of-2005-2010-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-classes-of-2005-2010-by-borough/data.csv"]
