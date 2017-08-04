import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j86k-5i43/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-property-data-commercial-and-retail-properties/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-property-data-commercial-and-retail-properties/data.csv"]
