import requests
r = requests.get("https://data.cityofnewyork.us/download/u2m4-wh3s/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-1-city-council-report-fy-2015/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/local-law-1-city-council-report-fy-2015/data.zip"]
