import requests
r = requests.get("https://data.cityofnewyork.us/api/views/krwf-eng6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sca-disqualified-firms/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sca-disqualified-firms/data.csv"]
