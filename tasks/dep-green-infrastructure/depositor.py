import requests
r = requests.get("https://data.cityofnewyork.us/download/496p-fwvq/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-green-infrastructure/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-green-infrastructure/data.zip"]
