import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nxvh-fkda/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grier-partnership-part-b-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grier-partnership-part-b-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv"]
