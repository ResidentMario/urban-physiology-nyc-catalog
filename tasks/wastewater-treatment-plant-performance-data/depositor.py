import requests
r = requests.get("https://data.cityofnewyork.us/download/hgue-hj96/application%2Fvnd.openxmlformats-officedocument.spreadsheetml.sheet")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plant-performance-data/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wastewater-treatment-plant-performance-data/data.xlsx"]
