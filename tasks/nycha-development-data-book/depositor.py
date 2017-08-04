import requests
r = requests.get("https://data.cityofnewyork.us/api/views/evjd-dqpz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-development-data-book/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-development-data-book/data.csv"]
