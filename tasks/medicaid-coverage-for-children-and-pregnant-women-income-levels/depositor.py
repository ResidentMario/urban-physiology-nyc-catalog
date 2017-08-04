import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4se9-u6dw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-coverage-for-children-and-pregnant-women-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-coverage-for-children-and-pregnant-women-income-levels/data.csv"]
