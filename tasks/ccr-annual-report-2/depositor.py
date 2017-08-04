import requests
r = requests.get("https://data.cityofnewyork.us/download/yjw6-uibq/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccr-annual-report-2/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccr-annual-report-2/data.xlsx"]
