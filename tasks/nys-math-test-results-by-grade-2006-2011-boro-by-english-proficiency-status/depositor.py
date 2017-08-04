import requests
r = requests.get("https://data.cityofnewyork.us/api/views/zpd4-gad8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nys-math-test-results-by-grade-2006-2011-boro-by-english-proficiency-status/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nys-math-test-results-by-grade-2006-2011-boro-by-english-proficiency-status/data.csv"]
