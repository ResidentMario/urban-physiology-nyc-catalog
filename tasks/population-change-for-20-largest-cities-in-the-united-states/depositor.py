import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6u6h-px7z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/population-change-for-20-largest-cities-in-the-united-states/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/population-change-for-20-largest-cities-in-the-united-states/data.csv"]
