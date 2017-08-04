import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rafb-6xry/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-programs-list-mayors-office/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-programs-list-mayors-office/data.csv"]
