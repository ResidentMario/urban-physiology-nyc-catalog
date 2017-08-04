import requests
r = requests.get("https://data.cityofnewyork.us/api/views/iz2q-9x8d/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-cellular-antenna-filings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-cellular-antenna-filings/data.csv"]
