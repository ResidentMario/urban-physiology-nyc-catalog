import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3spy-rjpw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportable-classroom-units-buildings-only/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportable-classroom-units-buildings-only/data.csv"]
