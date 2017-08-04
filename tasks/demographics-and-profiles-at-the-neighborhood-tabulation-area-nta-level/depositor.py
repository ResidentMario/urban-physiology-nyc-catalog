import requests
r = requests.get("https://data.cityofnewyork.us/download/hyuz-tij8/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographics-and-profiles-at-the-neighborhood-tabulation-area-nta-level/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/demographics-and-profiles-at-the-neighborhood-tabulation-area-nta-level/data.zip"]
