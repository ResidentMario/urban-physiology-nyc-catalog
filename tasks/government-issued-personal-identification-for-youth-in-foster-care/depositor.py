import requests
r = requests.get("https://data.cityofnewyork.us/download/n5e5-z493/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/government-issued-personal-identification-for-youth-in-foster-care/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/government-issued-personal-identification-for-youth-in-foster-care/data.xlsx"]
