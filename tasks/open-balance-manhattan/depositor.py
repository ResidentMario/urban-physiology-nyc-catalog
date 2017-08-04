import requests
r = requests.get("https://data.cityofnewyork.us/download/je66-se2r/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-manhattan/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-balance-manhattan/data.zip"]
