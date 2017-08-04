import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7zhs-43jt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-revenue-and-spending-summary-fy-1980-fy-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-revenue-and-spending-summary-fy-1980-fy-2013/data.csv"]
