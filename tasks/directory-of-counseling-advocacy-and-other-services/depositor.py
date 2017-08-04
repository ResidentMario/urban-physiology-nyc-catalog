import requests
r = requests.get("https://data.cityofnewyork.us/api/views/h922-jiy6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-counseling-advocacy-and-other-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-counseling-advocacy-and-other-services/data.csv"]
