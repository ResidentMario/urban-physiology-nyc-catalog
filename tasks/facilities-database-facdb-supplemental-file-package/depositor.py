import requests
r = requests.get("https://data.cityofnewyork.us/download/infj-99i7/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/facilities-database-facdb-supplemental-file-package/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/facilities-database-facdb-supplemental-file-package/data.zip"]
