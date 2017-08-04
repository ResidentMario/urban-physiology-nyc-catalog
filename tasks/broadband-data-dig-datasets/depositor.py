import requests
r = requests.get("https://data.cityofnewyork.us/download/ft4n-yqee/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/broadband-data-dig-datasets/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/broadband-data-dig-datasets/data.zip"]
