import requests
r = requests.get("https://data.cityofnewyork.us/download/ige5-v6sk/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lion-differences-file/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lion-differences-file/data.zip"]
