import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q8fg-j5sk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foil-report-all-markets-approved/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foil-report-all-markets-approved/data.csv"]
