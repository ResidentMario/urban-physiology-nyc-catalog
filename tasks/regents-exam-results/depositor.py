import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qk7d-gecv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/regents-exam-results/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/regents-exam-results/data.csv"]
