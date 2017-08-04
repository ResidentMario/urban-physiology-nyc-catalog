import requests
r = requests.get("https://data.cityofnewyork.us/api/views/d6ph-dqj8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grier-partnership-part-c-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grier-partnership-part-c-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv"]
