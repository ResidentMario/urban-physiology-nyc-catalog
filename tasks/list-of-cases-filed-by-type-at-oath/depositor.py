import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s7vy-wmm7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-cases-filed-by-type-at-oath/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-cases-filed-by-type-at-oath/data.csv"]
