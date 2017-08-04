import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8fj8-3sgg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceqr-project-milestones/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceqr-project-milestones/data.csv"]
