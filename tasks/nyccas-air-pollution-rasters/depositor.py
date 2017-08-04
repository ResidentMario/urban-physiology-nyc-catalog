import requests
r = requests.get("https://data.cityofnewyork.us/download/q68s-8qxv/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyccas-air-pollution-rasters/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyccas-air-pollution-rasters/data.zip"]
