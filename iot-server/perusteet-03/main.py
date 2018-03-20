from time import sleep
import requests

def request(call):
    response = requests.get("http://iot.olarinlukio.fi:5000/" + call)
    return response.text

request("database/opiskelija123n_taulukko/create/nouseva_numero")
arvo = 0
while True:
    arvo += 1
    print(arvo)
    request("database/opiskelija123n_taulukko/insert/" + str(arvo))
    sleep(2)
