import requests
r = requests.get("http://www.nyc.gov/html/dot/downloads/misc/2015_citybench.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-bench-locations/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-bench-locations/data.zip"]
