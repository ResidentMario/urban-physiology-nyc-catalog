import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yjsf-89ae/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-english-proficiency-status/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/english-language-arts-ela-test-results-by-grade-2006-2011-citywide-by-english-proficiency-status/data.csv"]
