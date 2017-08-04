import requests
r = requests.get("http://www.downtownny.com/sites/default/files/data/ADNY-Big-Apps-Data.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/alliance-for-downtown-new-york-big-apps-data/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/alliance-for-downtown-new-york-big-apps-data/data.zip"]
