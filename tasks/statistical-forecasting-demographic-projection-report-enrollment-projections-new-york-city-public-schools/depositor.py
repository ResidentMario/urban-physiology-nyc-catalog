import requests
r = requests.get("https://data.cityofnewyork.us/api/views/e649-r223/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/statistical-forecasting-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/statistical-forecasting-demographic-projection-report-enrollment-projections-new-york-city-public-schools/data.csv"]
