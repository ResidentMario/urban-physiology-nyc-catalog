import requests
r = requests.get("https://data.cityofnewyork.us/api/views/99br-frp6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-jobs-and-internships/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-jobs-and-internships/data.csv"]
