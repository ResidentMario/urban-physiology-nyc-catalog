import requests
r = requests.get("https://data.cityofnewyork.us/download/djj3-qxwf/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-staten-island/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-staten-island/data.zip"]
