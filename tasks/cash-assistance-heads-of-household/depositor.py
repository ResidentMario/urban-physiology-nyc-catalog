import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9ht6-44eh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-heads-of-household/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-heads-of-household/data.csv"]
