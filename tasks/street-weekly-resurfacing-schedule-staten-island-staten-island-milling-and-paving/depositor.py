import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cu8c-kkz7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-weekly-resurfacing-schedule-staten-island-staten-island-milling-and-paving/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-weekly-resurfacing-schedule-staten-island-staten-island-milling-and-paving/data.csv"]
