import requests
r = requests.get("http://207.251.86.229/nyc-links-cams/LinkSpeedQuery.txt")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/real-time-traffic-speed-data/data.pl", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/real-time-traffic-speed-data/data.pl"]
