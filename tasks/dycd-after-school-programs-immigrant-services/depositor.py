import requests
r = requests.get("https://data.cityofnewyork.us/api/views/zmut-au2w/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-immigrant-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-immigrant-services/data.csv"]
