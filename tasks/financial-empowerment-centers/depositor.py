import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dt2z-amuf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/financial-empowerment-centers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/financial-empowerment-centers/data.csv"]
