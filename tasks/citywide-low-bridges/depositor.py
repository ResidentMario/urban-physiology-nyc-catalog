import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/lowbridges_citywide_data_71309.kml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-low-bridges/data.kml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-low-bridges/data.kml"]
