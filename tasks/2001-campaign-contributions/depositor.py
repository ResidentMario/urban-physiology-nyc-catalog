import requests
r = requests.get("https://data.cityofnewyork.us/api/views/735p-zed8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2001-campaign-contributions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2001-campaign-contributions/data.csv"]
