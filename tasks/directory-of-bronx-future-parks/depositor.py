import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ssk8-4egt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-bronx-future-parks/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-bronx-future-parks/data.csv"]
