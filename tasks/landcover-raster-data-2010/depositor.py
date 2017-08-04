import requests
r = requests.get("https://data.cityofnewyork.us/download/9auy-76zt/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/landcover-raster-data-2010/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/landcover-raster-data-2010/data.zip"]
