import requests
r = requests.get("https://data.cityofnewyork.us/api/views/caav-grv8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/administrative-code-18-144-park-maintenance-report-payroll-data-fiscal-year-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/administrative-code-18-144-park-maintenance-report-payroll-data-fiscal-year-2016/data.csv"]
