import requests
r = requests.get("https://data.cityofnewyork.us/api/views/f46j-m4iq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-dop-family-adult-court-contact-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-dop-family-adult-court-contact-information/data.csv"]
