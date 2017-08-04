import requests
r = requests.get("http://a841-dotweb01.nyc.gov/datafeeds/ParkingReg/File%20description.pdf")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-regulation-locations-and-signs/data.pdf", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-regulation-locations-and-signs/data.pdf"]
