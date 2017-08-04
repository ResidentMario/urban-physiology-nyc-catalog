import requests
r = requests.get("https://data.cityofnewyork.us/api/views/r69u-62nw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adult-medicaid-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adult-medicaid-income-levels/data.csv"]
