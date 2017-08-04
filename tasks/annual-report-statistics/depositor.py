import requests
r = requests.get("https://data.cityofnewyork.us/download/s5c9-5mja/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-report-statistics/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-report-statistics/data.zip"]
