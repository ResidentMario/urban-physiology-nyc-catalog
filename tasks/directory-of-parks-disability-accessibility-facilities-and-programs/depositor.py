import requests
r = requests.get("https://data.cityofnewyork.us/api/views/e4ej-j6hn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-parks-disability-accessibility-facilities-and-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-parks-disability-accessibility-facilities-and-programs/data.csv"]
