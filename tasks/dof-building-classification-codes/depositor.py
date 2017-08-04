import requests
r = requests.get("http://nycprop.nyc.gov/nycproperty/help/hlpbldgcode.html")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-building-classification-codes/data.pl", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-building-classification-codes/data.pl"]
