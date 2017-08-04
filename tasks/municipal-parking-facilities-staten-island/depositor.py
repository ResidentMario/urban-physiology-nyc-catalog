import requests
r = requests.get("http://a841-dotweb01.nyc.gov/datafeeds/SIParking.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/municipal-parking-facilities-staten-island/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/municipal-parking-facilities-staten-island/data.xml"]
