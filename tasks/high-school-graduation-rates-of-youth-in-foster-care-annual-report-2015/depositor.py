import requests
r = requests.get("https://data.cityofnewyork.us/download/abgy-h8ag/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/high-school-graduation-rates-of-youth-in-foster-care-annual-report-2015/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/high-school-graduation-rates-of-youth-in-foster-care-annual-report-2015/data.xlsx"]
