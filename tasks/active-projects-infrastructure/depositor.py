import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rukc-mmqu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-infrastructure/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-projects-infrastructure/data.csv"]
