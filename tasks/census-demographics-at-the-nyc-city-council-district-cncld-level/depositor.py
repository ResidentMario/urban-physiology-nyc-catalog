import requests
r = requests.get("https://data.cityofnewyork.us/download/ye4r-qpmp/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-nyc-city-council-district-cncld-level/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-nyc-city-council-district-cncld-level/data.xlsx"]
