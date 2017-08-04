import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3mim-bd27/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-regular-hs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-regular-hs/data.csv"]
