import requests
r = requests.get("https://data.cityofnewyork.us/api/views/t6g4-rw7k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rate-at-which-the-ccrb-made-findings-on-the-merits/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rate-at-which-the-ccrb-made-findings-on-the-merits/data.csv"]
