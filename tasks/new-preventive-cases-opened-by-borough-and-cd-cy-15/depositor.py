import requests
r = requests.get("https://data.cityofnewyork.us/download/a2ju-qb9a/application%2Fvnd.ms-excel")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-preventive-cases-opened-by-borough-and-cd-cy-15/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-preventive-cases-opened-by-borough-and-cd-cy-15/data.xlsx"]
