import requests
r = requests.get("https://data.cityofnewyork.us/download/5unr-w4sc/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-nyc-community-district-cd-level/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-nyc-community-district-cd-level/data.xlsx"]
