import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gffu-ps8j/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/income-by-type-of-income-and-agi-range/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/income-by-type-of-income-and-agi-range/data.csv"]
