import requests
r = requests.get("https://data.cityofnewyork.us/download/qs4p-vs2w/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/roadbed-pointer-list-rpl/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/roadbed-pointer-list-rpl/data.zip"]
