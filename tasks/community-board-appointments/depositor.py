import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3gkd-ddzn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-board-appointments/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-board-appointments/data.csv"]
