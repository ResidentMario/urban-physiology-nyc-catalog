import requests
r = requests.get("http://www.nycgovparks.org/bigapps/DPR_Kayak_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-water-trail-kayak-and-canoe-launch-sites/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-water-trail-kayak-and-canoe-launch-sites/data.xml"]
