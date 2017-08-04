import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yz7z-iupz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nys-math-test-results-by-grade-2006-2011-district-by-gender/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nys-math-test-results-by-grade-2006-2011-district-by-gender/data.csv"]
