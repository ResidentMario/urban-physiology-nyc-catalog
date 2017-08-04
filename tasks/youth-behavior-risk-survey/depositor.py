import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3qty-g4aq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/youth-behavior-risk-survey/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/youth-behavior-risk-survey/data.csv"]
