import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wibz-uqui/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypl-branch-services-staten-island/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypl-branch-services-staten-island/data.csv"]
