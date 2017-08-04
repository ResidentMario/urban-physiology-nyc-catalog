import requests
r = requests.get("https://data.cityofnewyork.us/api/views/i3a3-qxkf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-district-poll-sites/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-district-poll-sites/data.csv"]
