import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ijru-c88e/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hose-nozzle-and-sprayer-survey/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hose-nozzle-and-sprayer-survey/data.csv"]
