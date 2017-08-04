import requests
r = requests.get("https://data.cityofnewyork.us/api/views/azp6-hepu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/licensing-center-customer-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/licensing-center-customer-information/data.csv"]
