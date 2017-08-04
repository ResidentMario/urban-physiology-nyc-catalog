import requests
r = requests.get("https://data.cityofnewyork.us/download/7q5y-m6mr/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographics-and-profiles-at-the-public-use-microdata-area-puma-subarea-level/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographics-and-profiles-at-the-public-use-microdata-area-puma-subarea-level/data.zip"]
