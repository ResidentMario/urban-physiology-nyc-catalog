import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gzdv-qiga/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/completed-percent-for-art-projects-with-artist-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/completed-percent-for-art-projects-with-artist-information/data.csv"]
