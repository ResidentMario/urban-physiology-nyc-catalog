import requests
r = requests.get("https://data.cityofnewyork.us/download/3m2q-9maw/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/child-welfare-indicators-annual-and-quarterly-report-indicators/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/child-welfare-indicators-annual-and-quarterly-report-indicators/data.zip"]
