import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ect6-rj3p/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/safety-net-assistance-sna-recipients/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/safety-net-assistance-sna-recipients/data.csv"]
