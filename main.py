import requests

proxy = '	158.255.215.50:8080'

response = requests.get("https://httpbin.org/ip", proxies={ 'http':proxy, 'https': proxy}, timeout=3)
print(response.status_code())
