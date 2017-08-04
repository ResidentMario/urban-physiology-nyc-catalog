import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_taxicab_metershops.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-metershops/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-metershops/data.xls"]
