import requests
r = requests.get("https://data.cityofnewyork.us/api/views/phth-xf25/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-2006-2012-school-swd/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-2006-2012-school-swd/data.csv"]
