import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xgse-vmv6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-citys-school-age-and-65-and-over-populations-by-borough-1950-2040/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-citys-school-age-and-65-and-over-populations-by-borough-1950-2040/data.csv"]
