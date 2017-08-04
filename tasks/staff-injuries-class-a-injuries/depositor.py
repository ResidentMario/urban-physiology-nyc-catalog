import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7hi3-kaps/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/staff-injuries-class-a-injuries/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/staff-injuries-class-a-injuries/data.csv"]
