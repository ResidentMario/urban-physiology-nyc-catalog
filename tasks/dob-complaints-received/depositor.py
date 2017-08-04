import requests
r = requests.get("https://data.cityofnewyork.us/api/views/eabe-havv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-complaints-received/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-complaints-received/data.csv"]
