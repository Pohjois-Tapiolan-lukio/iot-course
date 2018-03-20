import requests

response = requests.get("http://iot.olarinlukio.fi:5000/heippa")
print(response.text)
