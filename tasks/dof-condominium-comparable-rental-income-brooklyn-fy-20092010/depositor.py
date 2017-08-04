import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w6yt-hctp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-brooklyn-fy-20092010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-brooklyn-fy-20092010/data.csv"]
