import requests
r = requests.get("https://data.cityofnewyork.us/api/views/36hn-wea6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-osy-out-of-school-youth-employment-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-osy-out-of-school-youth-employment-programs/data.csv"]
