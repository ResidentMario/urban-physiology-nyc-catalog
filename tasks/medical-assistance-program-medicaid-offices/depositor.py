import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fzk8-3ynb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medical-assistance-program-medicaid-offices/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medical-assistance-program-medicaid-offices/data.csv"]
