import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6dgq-4h88/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/study-material-for-certificate-of-fitness/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/study-material-for-certificate-of-fitness/data.csv"]
