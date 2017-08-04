import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vz8c-29aj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-enrollment-offices/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-enrollment-offices/data.csv"]
