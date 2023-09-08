import requests
import pandas as pd
from datetime import datetime
import time

k = 10
while True:
#while k == 10:
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    tabela = pd.read_excel("C:/Users/Erico/Desktop/Crypto/cotacao.xlsx")
    tabela.loc[0, "Moeda"] = "Dolar"
    tabela.loc[1, "Moeda"] = "Real"
    tabela.loc[2, "Moeda"] = "BTC"
    tabela.loc[0, "Cotação"] = float(cotacao_dolar)
    tabela.loc[1, "Cotação"] = float(cotacao_euro)
    tabela.loc[2, "Cotação"] = float(cotacao_btc)
    print(float(cotacao_btc))
    tabela.loc[0, "Data Última Atualização"] = datetime.now()

    tabela.to_excel("C:/Users/Erico/Desktop/Crypto/cotacao.xlsx", index=False)
    print(f"Cotação Atualizada. {datetime.now()}")
    # k = 1
    time.sleep(10)