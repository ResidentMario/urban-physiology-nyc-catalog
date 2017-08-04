import requests
r = requests.get("https://data.cityofnewyork.us/download/gx5n-2nma/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/report-on-youth-in-foster-care-ll-46-2015/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/report-on-youth-in-foster-care-ll-46-2015/data.xlsx"]
