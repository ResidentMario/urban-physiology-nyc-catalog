import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mbym-vp3s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-citywide-classes-of-2005-2011-ethnicity/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/graduation-outcomes-citywide-classes-of-2005-2011-ethnicity/data.csv"]
