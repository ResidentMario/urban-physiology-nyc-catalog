import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9gmp-f9x2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-the-grier-partnership-part-c/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographic-projection-report-enrollment-projections-new-york-city-public-schools-prepared-by-the-grier-partnership-part-c/data.csv"]
