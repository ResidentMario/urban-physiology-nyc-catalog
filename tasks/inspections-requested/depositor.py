import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n4tc-j6kh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inspections-requested/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inspections-requested/data.csv"]
