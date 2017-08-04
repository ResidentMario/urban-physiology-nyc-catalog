import requests
r = requests.get("https://developer.foursquare.com/")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foursquare-api/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foursquare-api/data.xml"]
