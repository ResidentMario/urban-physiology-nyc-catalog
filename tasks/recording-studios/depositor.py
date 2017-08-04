import requests
r = requests.get("https://data.cityofnewyork.us/download/9ixa-eggw/application%2Fxml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recording-studios/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recording-studios/data.xml"]
