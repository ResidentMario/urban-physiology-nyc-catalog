import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vp38-q6cf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-service-hotlines/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-service-hotlines/data.csv"]
