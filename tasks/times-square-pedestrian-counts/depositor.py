import requests
r = requests.get("https://data.cityofnewyork.us/download/dv6z-emb2/application%2Fvnd.ms-office")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-pedestrian-counts/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-pedestrian-counts/data.xls"]
