import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b2gb-nkrq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citizen-emergency-response-team-cert/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citizen-emergency-response-team-cert/data.csv"]
