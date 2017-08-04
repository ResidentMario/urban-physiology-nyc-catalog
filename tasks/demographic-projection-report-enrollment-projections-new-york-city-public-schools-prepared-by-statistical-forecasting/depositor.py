import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xzy8-qqgf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-statistical-forecasting/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-statistical-forecasting/data.csv"]
