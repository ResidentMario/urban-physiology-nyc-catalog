import requests
r = requests.get("https://data.cityofnewyork.us/download/dgm3-gggb/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-street-reconstruction-10-year-plan/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-street-reconstruction-10-year-plan/data.zip"]
