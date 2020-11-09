import requests

response = requests.put('http://127.0.0.1:8000/api/v1/investor/passport?investor_id=1', files={'file': open('test.jpg', 'rb')})
print(response.content)
