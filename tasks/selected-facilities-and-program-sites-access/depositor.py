import requests
r = requests.get("https://data.cityofnewyork.us/download/ibjs-7vdf/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/selected-facilities-and-program-sites-access/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/selected-facilities-and-program-sites-access/data.zip"]
