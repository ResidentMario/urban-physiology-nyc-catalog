import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3cn8-i54i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-district-75-special-ed/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-district-75-special-ed/data.csv"]
