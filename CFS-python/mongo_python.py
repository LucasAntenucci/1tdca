#!/usr/bin/env python3

import pymongo


#Conectando ao Banco de dados
client = pymongo.MongoClient('localhost', 27017)

#enviando a informacao que queremos criar a Base Fiap
db = client.Fiap
#collection = db.create_collection("alunos")

#inserindo dados

#insert one
'''resultado = db.client.Fiap.alunos.find_one({'nome_aluno':'Lucas Cunha'})
if resultado: 
    print(resultado)
else:
    print("Nada foi encontrado")'''

'''resultado = db.client.Fiap.alunos.find({})
for dado in resultado:
    print(dado['email_aluno'])'''

#resultado = db.client.Fiap.alunos.delete_one({'idade_aluno': { '$gt' : '30'}})

resultado = db.client.Fiap.alunos.update_one({'nome_aluno':'Alberico Japa'},{'$set': {'idade_aluno':'40'}})
'''db.client.Fiap.alunos.insert_many(
    [
        {
            'nome_aluno':'Marcos Cortez',
            'email_aluno':'cortez@fiap.com.br',
            'idade_aluno':'22' 
        },
        {
            'nome_aluno':'Gustavo Lima',
            'email_aluno':'glima@fiap.com.br',
            'idade_aluno':'35'
        },
        {
            'nome_aluno':'Alberico Japa',
            'email_aluno':'japa@fiap.com.br',
            'idade_aluno':'30'

        }

    ]
)'''
