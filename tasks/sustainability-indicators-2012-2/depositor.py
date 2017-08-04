import requests
r = requests.get("https://data.cityofnewyork.us/download/vnwz-ihnf/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sustainability-indicators-2012-2/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sustainability-indicators-2012-2/data.xlsx"]
