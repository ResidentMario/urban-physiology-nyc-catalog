import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w9ak-ipjd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-now-build-job-application-filings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-now-build-job-application-filings/data.csv"]
