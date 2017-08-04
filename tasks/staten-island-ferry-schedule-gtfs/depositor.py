import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/siferry-gtfs.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/staten-island-ferry-schedule-gtfs/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/staten-island-ferry-schedule-gtfs/data.zip"]
