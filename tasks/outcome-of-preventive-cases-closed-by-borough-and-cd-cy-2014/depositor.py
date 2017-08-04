import requests
r = requests.get("https://data.cityofnewyork.us/download/q663-gvx6/application%2Fvnd.ms-excel")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/outcome-of-preventive-cases-closed-by-borough-and-cd-cy-2014/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/outcome-of-preventive-cases-closed-by-borough-and-cd-cy-2014/data.xlsx"]
