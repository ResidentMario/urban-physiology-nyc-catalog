import requests
r = requests.get("https://data.cityofnewyork.us/api/views/siju-6isf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/math-test-results-2006-2012-district-ell/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/math-test-results-2006-2012-district-ell/data.csv"]
