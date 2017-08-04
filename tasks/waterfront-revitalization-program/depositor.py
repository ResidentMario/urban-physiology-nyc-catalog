import requests
r = requests.get("https://data.cityofnewyork.us/download/cbn4-bn4p/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/waterfront-revitalization-program/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/waterfront-revitalization-program/data.zip"]
