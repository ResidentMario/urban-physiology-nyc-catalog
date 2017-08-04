import requests
r = requests.get("https://data.cityofnewyork.us/api/views/37fm-7uaa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-customer-contact-centers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-customer-contact-centers/data.csv"]
