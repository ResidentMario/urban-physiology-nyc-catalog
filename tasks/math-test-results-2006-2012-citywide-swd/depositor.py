import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ufu7-zp25/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/math-test-results-2006-2012-citywide-swd/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/math-test-results-2006-2012-citywide-swd/data.csv"]
