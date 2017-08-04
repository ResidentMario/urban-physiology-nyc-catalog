import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mrxb-9w9v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-youth-employment-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-youth-employment-programs/data.csv"]
