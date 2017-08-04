import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nadh-kjkc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-community-car-service-bases/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-community-car-service-bases/data.csv"]
