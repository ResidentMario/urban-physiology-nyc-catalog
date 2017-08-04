import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8586-3zfm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-under-construction/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-under-construction/data.csv"]
