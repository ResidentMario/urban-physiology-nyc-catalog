import requests
r = requests.get("https://data.cityofnewyork.us/api/views/myn9-hwsy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/exemption-classification-codes/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/exemption-classification-codes/data.csv"]
