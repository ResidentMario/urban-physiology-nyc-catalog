import requests
r = requests.get("https://data.cityofnewyork.us/api/views/d3ge-anaz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-10-class-size-school-level-detail/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-10-class-size-school-level-detail/data.csv"]
