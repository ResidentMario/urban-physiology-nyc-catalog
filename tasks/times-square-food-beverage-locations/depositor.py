import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kh2m-kcyz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-food-beverage-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-food-beverage-locations/data.csv"]
