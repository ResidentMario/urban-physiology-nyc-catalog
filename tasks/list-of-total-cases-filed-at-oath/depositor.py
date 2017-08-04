import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j8uz-fizu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-total-cases-filed-at-oath/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-total-cases-filed-at-oath/data.csv"]
