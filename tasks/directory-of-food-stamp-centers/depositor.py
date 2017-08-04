import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tc6u-8rnp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-food-stamp-centers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-food-stamp-centers/data.csv"]
