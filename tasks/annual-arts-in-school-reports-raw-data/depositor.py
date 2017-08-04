import requests
r = requests.get("https://data.cityofnewyork.us/download/vdgp-ddvg/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-arts-in-school-reports-raw-data/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-arts-in-school-reports-raw-data/data.zip"]
