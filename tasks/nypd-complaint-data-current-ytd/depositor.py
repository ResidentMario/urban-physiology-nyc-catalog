import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5uac-w243/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-complaint-data-current-ytd/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-complaint-data-current-ytd/data.csv"]
