import requests
r = requests.get("https://data.cityofnewyork.us/download/sf3b-xntp/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bike-counts/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bike-counts/data.zip"]
