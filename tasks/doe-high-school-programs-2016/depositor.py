import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ge8j-uqbf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-programs-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-programs-2016/data.csv"]
