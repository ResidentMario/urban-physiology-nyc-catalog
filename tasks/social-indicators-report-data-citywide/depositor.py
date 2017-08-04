import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gysw-j2f3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/social-indicators-report-data-citywide/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/social-indicators-report-data-citywide/data.csv"]
