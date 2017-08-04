import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s2zm-f47y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/prenatal-care-services-monthly-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/prenatal-care-services-monthly-income-levels/data.csv"]
