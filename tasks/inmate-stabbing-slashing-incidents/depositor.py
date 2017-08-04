import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hve5-8z68/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-stabbing-slashing-incidents/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-stabbing-slashing-incidents/data.csv"]
