import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gcvr-n8qw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-mathematics-exam-by-school/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-mathematics-exam-by-school/data.csv"]
