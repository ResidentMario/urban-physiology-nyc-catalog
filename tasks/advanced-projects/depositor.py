import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yiqb-mq9h/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/advanced-projects/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/advanced-projects/data.csv"]
