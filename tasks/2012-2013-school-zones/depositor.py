import requests
r = requests.get("https://data.cityofnewyork.us/download/4szu-rxzq/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2012-2013-school-zones/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2012-2013-school-zones/data.zip"]
