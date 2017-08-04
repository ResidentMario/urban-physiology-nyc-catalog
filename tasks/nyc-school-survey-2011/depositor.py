import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/11FE72CE-1313-4C82-88B1-C9FA53BE6842/0/2011datafilesonline.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2011/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2011/data.zip"]
