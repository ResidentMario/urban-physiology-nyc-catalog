import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sd9s-b3hd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/average-days-for-the-ccrb-to-close-case/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/average-days-for-the-ccrb-to-close-case/data.csv"]
