import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_medallion_agents.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-agents/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-agents/data.xls"]
