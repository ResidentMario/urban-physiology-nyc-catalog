import requests
r = requests.get("https://data.cityofnewyork.us/download/eznj-hdma/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-bronx/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-bronx/data.zip"]
