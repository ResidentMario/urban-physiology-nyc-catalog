import requests
r = requests.get("https://data.cityofnewyork.us/api/views/366m-74zg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wic-income-eligibility/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wic-income-eligibility/data.csv"]
