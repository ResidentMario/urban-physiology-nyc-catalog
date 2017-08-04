import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xubg-57si/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-now-safety-facades-compliance-filings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-now-safety-facades-compliance-filings/data.csv"]
