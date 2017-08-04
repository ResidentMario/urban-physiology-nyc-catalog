import requests
r = requests.get("https://data.cityofnewyork.us/download/2jnq-tef6/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/detention-and-placement-incident-reports/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/detention-and-placement-incident-reports/data.zip"]
