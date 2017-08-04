import requests
r = requests.get("https://data.cityofnewyork.us/api/views/35f6-8qd2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/denied-registrants-in-the-wholesale-markets/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/denied-registrants-in-the-wholesale-markets/data.csv"]
