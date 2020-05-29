import requests
import json

headers = {'Content-Type': 'application/json'}

url = 'http://0.0.0.0:8080/train'
body = json.dumps({'method': 'random_forest'})
resp = requests.post(url, data=body, headers=headers)
print(resp.status_code)
print(resp.json())

url = 'http://0.0.0.0:8080/predict'
body = json.dumps({'method': 'random_forest', 'data': [5.1, 3.5, 1.4, 0.2]})
resp = requests.post(url, data=body, headers=headers)
print(resp.status_code)
print(resp.json())
