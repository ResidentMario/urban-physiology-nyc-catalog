import requests
r = requests.get("https://data.cityofnewyork.us/download/gs56-euca/application%2Fxml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/broadway-events-calendar/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/broadway-events-calendar/data.xml"]
