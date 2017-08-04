import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nstm-kb7u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/60-month-converted-to-safety-net-sn-recipients/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/60-month-converted-to-safety-net-sn-recipients/data.csv"]
