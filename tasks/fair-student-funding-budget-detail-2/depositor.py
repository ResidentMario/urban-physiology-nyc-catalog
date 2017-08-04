import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nbgq-j9jt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fair-student-funding-budget-detail-2/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fair-student-funding-budget-detail-2/data.csv"]
