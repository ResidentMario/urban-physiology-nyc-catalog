import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nuxu-5fjs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-weekly-resurfacing-schedule-queens/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-weekly-resurfacing-schedule-queens/data.csv"]
