import requests
r = requests.get("https://data.cityofnewyork.us/download/qb3k-n8mm/application%2Fxml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/filming-locations-scenes-from-the-city/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/filming-locations-scenes-from-the-city/data.xml"]
