import requests
r = requests.get("https://data.cityofnewyork.us/download/2v4z-66xt/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lion/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lion/data.zip"]
