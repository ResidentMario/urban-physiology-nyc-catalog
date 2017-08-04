import requests
r = requests.get("https://data.cityofnewyork.us/download/i8iw-xf4u/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zip-code-boundaries/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zip-code-boundaries/data.zip"]
