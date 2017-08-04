import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yti5-bbws/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drought-regulation-penalty-schedule/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drought-regulation-penalty-schedule/data.csv"]
