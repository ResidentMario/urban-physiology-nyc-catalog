import requests
r = requests.get("https://data.cityofnewyork.us/download/nzih-r6xb/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurement-by-method/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/procurement-by-method/data.xlsx"]
