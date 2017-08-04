import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fu34-wamz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-state-and-federal-categorical-aid-fy-1980-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-state-and-federal-categorical-aid-fy-1980-2013/data.csv"]
