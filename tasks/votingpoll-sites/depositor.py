import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mifw-tguq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/votingpoll-sites/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/votingpoll-sites/data.csv"]
