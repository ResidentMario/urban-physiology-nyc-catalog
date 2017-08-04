import requests
r = requests.get("https://data.cityofnewyork.us/download/fmhd-mfkw/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/clean-air-survey-content-2009/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/clean-air-survey-content-2009/data.zip"]
