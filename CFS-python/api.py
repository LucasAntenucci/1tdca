#!/usr/bin/env python


from pprint import pprint
import requests
#informacoes = '{"Nome":"Ryan", "Sobrenome" : "Creese", "Idade" : "65", "Especialidade" : "CobraKai"}'
consulta = requests.delete("https://fiap1tdca-83f3c-default-rtdb.firebaseio.com/-NBm-2-obp_GcX80d5C_/.json")
pprint(consulta.status_code)
pprint(consulta.headers)
pprint(consulta.json())