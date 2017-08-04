import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j7wr-gf2w/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-gender/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-gender/data.csv"]
