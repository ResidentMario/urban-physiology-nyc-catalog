import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j6ik-kjbs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-tennis-courts-with-online-registration/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-tennis-courts-with-online-registration/data.csv"]
