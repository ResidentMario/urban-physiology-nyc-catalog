import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g9ub-hrve/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-public-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-public-buildings/data.csv"]
