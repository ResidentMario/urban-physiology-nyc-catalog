import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ic2k-etms/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/social-indicators-report-data-by-neighborhood-tabulation-districts/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/social-indicators-report-data-by-neighborhood-tabulation-districts/data.csv"]
