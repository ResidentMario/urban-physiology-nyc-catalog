import requests
r = requests.get("https://data.cityofnewyork.us/download/xg3x-h3g7/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/placements-by-community-district-cd/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/placements-by-community-district-cd/data.xlsx"]
