import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q5x3-7piv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-syep-summer-youth-employment-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-syep-summer-youth-employment-programs/data.csv"]
