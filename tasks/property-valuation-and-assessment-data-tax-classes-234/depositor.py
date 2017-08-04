import requests
r = requests.get("https://data.cityofnewyork.us/download/cqds-77ys/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data-tax-classes-234/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/property-valuation-and-assessment-data-tax-classes-234/data.zip"]
