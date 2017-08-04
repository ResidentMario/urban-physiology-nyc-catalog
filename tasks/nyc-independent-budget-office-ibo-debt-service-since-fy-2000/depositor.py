import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6ggx-itps/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-debt-service-since-fy-2000/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-debt-service-since-fy-2000/data.csv"]
