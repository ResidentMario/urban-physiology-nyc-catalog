import requests
r = requests.get("https://data.cityofnewyork.us/api/views/svqu-rx2s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-preladpt/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-preladpt/data.csv"]
