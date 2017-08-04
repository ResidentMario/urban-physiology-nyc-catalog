import requests
r = requests.get("https://data.cityofnewyork.us/download/vy67-bzq3/application%2Fvnd.ms-excel")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2014-2015-school-quality-reports-results-for-elementary-middle-and-k-8-schools/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2014-2015-school-quality-reports-results-for-elementary-middle-and-k-8-schools/data.xlsx"]
