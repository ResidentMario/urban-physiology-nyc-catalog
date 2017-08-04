import requests
r = requests.get("https://data.cityofnewyork.us/download/p23h-ci72/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/greenstreets/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/greenstreets/data.zip"]
