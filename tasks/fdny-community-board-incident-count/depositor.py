import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rtc6-e7ff/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-community-board-incident-count/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-community-board-incident-count/data.csv"]
