import requests
r = requests.get("https://data.cityofnewyork.us/download/twim-r7xp/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/franchise-and-concession-review-committee/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/franchise-and-concession-review-committee/data.xlsx"]
