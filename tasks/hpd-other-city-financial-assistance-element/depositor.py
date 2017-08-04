import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hujx-6z5u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-other-city-financial-assistance-element/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hpd-other-city-financial-assistance-element/data.csv"]
