import requests
r = requests.get("https://data.cityofnewyork.us/api/views/crns-fw6u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nycha-community-facilities/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nycha-community-facilities/data.csv"]
