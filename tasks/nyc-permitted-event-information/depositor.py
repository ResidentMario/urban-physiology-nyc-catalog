import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tvpp-9vvx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-permitted-event-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-permitted-event-information/data.csv"]
