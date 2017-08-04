import requests
r = requests.get("https://www.nycgovparks.org/xml/events_300_rss.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-parks-public-events-upcoming-14-days/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-parks-public-events-upcoming-14-days/data.xml"]
