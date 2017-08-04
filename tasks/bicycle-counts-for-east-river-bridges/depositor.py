import requests
r = requests.get("https://data.cityofnewyork.us/download/gua4-p9wg/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-counts-for-east-river-bridges/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-counts-for-east-river-bridges/data.zip"]
