import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/bike_shelters.kml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-shelters/data.kml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bicycle-shelters/data.kml"]
