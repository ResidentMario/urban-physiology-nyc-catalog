import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s3k6-pzi2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2017/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2017/data.csv"]
