import requests
r = requests.get("https://data.cityofnewyork.us/download/rnjn-x48k/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/abuseneglect-by-community-district-cd/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/abuseneglect-by-community-district-cd/data.xlsx"]
