import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/local_truck_routes_nyc.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-local-truck-routes/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-local-truck-routes/data.zip"]
