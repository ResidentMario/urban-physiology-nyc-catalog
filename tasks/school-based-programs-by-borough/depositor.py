import requests
r = requests.get("https://data.cityofnewyork.us/api/views/esmb-8zkm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-based-programs-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-based-programs-by-borough/data.csv"]
