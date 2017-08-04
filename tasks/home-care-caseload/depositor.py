import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xjur-zbxw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/home-care-caseload/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/home-care-caseload/data.csv"]
