import requests
r = requests.get("https://data.cityofnewyork.us/api/views/thqd-deec/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-recipients-since-1955/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-recipients-since-1955/data.csv"]
