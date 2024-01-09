import requests
import csv
import concurrent.futures

proxylist = []

with open('http.csv','r')  as f:
  reader = csv.reader(f)
  for row in reader:
    proxylist.append(row[0])
    
print(len(proxylist))


def extract(proxy):
  try:
    r = requests.get('https://httpbin.org/ip', proxies={'http':proxy, 'https':proxy}, timeout=2)
    print(r.json(), ' - working')
  except:
    pass
  return proxy

with  concurrent.futures.ThreadPoolExecutor() as exector:
  exector.map(extract, proxylist)
