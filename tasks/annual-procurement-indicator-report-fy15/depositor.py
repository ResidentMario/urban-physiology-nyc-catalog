import requests
r = requests.get("https://data.cityofnewyork.us/download/qiwn-t99b/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-procurement-indicator-report-fy15/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annual-procurement-indicator-report-fy15/data.zip"]
