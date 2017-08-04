import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qpm9-j523/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-business-improvement-districts/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-business-improvement-districts/data.csv"]
