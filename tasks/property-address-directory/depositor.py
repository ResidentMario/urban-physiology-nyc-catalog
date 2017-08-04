import requests
r = requests.get("https://data.cityofnewyork.us/download/bc8t-ecyu/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-address-directory/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-address-directory/data.zip"]
