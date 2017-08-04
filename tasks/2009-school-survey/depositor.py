import requests
r = requests.get("https://data.cityofnewyork.us/download/ens7-ac7e/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-school-survey/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-school-survey/data.zip"]
