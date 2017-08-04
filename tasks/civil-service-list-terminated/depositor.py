import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qu8g-sxqf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-service-list-terminated/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-service-list-terminated/data.csv"]
