import requests
r = requests.get("https://data.cityofnewyork.us/api/views/grbs-nm2g/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/village-alliance-merchants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/village-alliance-merchants/data.csv"]
