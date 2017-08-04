import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7iqz-npua/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-citywide-special-events/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-citywide-special-events/data.csv"]
