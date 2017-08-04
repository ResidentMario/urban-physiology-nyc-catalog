import requests
r = requests.get("https://data.cityofnewyork.us/download/my58-k6an/application%2Fvnd.ms-excel")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/green-project-checklist/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/green-project-checklist/data.xls"]
