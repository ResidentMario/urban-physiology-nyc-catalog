import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ph7v-u5f3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/vision-zero-base-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/vision-zero-base-report/data.csv"]
