import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k397-673e/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-payroll-data-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-payroll-data-fiscal-year/data.csv"]
