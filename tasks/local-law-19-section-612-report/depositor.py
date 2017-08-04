import requests
r = requests.get("https://data.cityofnewyork.us/download/29i8-bmct/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-19-section-612-report/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-19-section-612-report/data.xlsx"]
