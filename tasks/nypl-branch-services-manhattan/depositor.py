import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3nja-bsch/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypl-branch-services-manhattan/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypl-branch-services-manhattan/data.csv"]
