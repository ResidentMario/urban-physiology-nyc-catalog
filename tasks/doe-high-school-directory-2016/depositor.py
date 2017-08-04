import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7crd-d9xh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2016/data.csv"]
