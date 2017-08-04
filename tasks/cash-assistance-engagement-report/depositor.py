import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hb7y-b986/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-engagement-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-engagement-report/data.csv"]
