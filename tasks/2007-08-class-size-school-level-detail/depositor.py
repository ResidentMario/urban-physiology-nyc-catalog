import requests
r = requests.get("https://data.cityofnewyork.us/api/views/i8ys-e4pm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2007-08-class-size-school-level-detail/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2007-08-class-size-school-level-detail/data.csv"]
