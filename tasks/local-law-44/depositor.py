import requests
r = requests.get("https://data.cityofnewyork.us/download/igkv-8cju/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-44/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-44/data.zip"]
