import requests
r = requests.get("https://data.cityofnewyork.us/api/views/33db-aeds/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-hra-administered-medicaid-enrollees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-hra-administered-medicaid-enrollees/data.csv"]
