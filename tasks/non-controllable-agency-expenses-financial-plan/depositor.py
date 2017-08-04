import requests
r = requests.get("https://data.cityofnewyork.us/api/views/m6yw-2k8k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/non-controllable-agency-expenses-financial-plan/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/non-controllable-agency-expenses-financial-plan/data.csv"]
