import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7zb8-7bpk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-tax-rates-by-tax-class/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-tax-rates-by-tax-class/data.csv"]
