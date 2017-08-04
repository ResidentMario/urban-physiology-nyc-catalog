import requests
r = requests.get("https://data.cityofnewyork.us/download/qpsp-bm9z/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data-tax-class/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data-tax-class/data.zip"]
