import requests
r = requests.get("https://data.cityofnewyork.us/download/jfju-ynrr/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-point-locations/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-point-locations/data.zip"]
