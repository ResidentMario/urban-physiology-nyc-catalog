import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ipc3-2nbm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/personal-income-by-agi-range/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/personal-income-by-agi-range/data.csv"]
