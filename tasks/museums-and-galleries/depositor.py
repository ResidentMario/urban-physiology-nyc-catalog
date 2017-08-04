import requests
r = requests.get("https://data.cityofnewyork.us/download/kcrm-j9hh/application%2Fxml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/museums-and-galleries/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/museums-and-galleries/data.xml"]
