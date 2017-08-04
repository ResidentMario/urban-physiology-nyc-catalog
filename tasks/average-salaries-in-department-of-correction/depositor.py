import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pf7i-ims3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/average-salaries-in-department-of-correction/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/average-salaries-in-department-of-correction/data.csv"]
