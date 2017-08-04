import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2r9r-m6j4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-health-survey/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-health-survey/data.csv"]
