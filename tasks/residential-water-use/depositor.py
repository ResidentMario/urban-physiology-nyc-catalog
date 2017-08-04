import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xqzj-nd8g/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/residential-water-use/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/residential-water-use/data.csv"]
