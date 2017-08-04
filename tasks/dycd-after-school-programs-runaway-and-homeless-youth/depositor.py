import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ujsc-un6m/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-runaway-and-homeless-youth/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-runaway-and-homeless-youth/data.csv"]
