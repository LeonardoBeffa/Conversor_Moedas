import requests

def convert_moeda(moedas_origem,moeda_dest):
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas_origem}-{moeda_dest}"
    req = requests.get(url)
    cot = req.json()[f"{moedas_origem}{moeda_dest}"]["bid"]
    return cot
