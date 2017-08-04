import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j34j-vqvt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-monthly-response-times/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-monthly-response-times/data.csv"]
