import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hjae-yuav/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-toilets-in-public-parks/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-toilets-in-public-parks/data.csv"]
