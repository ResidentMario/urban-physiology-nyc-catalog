import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k26i-s5bd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grand-central-partnership-gcp-business-directory/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grand-central-partnership-gcp-business-directory/data.csv"]
