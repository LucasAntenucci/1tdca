#!/usr/bin/env python

from pprint import pprint
import requests

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CLP-BRL")

#print(cotacao)
#pprint(cotacao.json())

cotacao_dolar = cotacao.json()['USDBRL']['bid']
print(cotacao_dolar)in