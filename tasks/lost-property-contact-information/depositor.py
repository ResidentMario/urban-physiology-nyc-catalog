import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dg7a-jiz2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lost-property-contact-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lost-property-contact-information/data.csv"]
