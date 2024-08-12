import requests
from datetime import datetime

req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

req_dic = req.json()
cotacao_dolar = req_dic["USDBRL"]["bid"]
cotacao_euro = req_dic["EURBRL"]["bid"]
cotacao_btc = req_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")