import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sci4-yqgk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/daily-report-of-single-adult-and-family-intake/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/daily-report-of-single-adult-and-family-intake/data.csv"]
