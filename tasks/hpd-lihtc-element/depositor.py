import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ujzq-562i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-lihtc-element/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-lihtc-element/data.csv"]
