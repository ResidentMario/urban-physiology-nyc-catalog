import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6m3u-8rbh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/upcoming-contracts-to-be-awarded-cap/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/upcoming-contracts-to-be-awarded-cap/data.csv"]
