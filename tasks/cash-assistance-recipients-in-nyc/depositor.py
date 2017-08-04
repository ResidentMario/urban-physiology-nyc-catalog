import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qtrj-g3nm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-recipients-in-nyc/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-recipients-in-nyc/data.csv"]
