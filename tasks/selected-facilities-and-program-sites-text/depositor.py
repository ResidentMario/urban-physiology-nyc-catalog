import requests
r = requests.get("https://data.cityofnewyork.us/download/94qw-aaee/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/selected-facilities-and-program-sites-text/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/selected-facilities-and-program-sites-text/data.zip"]
