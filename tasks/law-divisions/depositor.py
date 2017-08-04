import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4se9-mk53/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-divisions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-divisions/data.csv"]
