import requests
r = requests.get("https://data.cityofnewyork.us/download/dqkt-8x6u/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-zones-2011-2012/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-zones-2011-2012/data.zip"]
