import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4g4r-7dfb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2006-07-class-size-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2006-07-class-size-by-borough/data.csv"]
