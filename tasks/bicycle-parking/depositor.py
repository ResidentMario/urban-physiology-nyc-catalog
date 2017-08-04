import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/2013-cityracks-shp.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-parking/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-parking/data.zip"]
