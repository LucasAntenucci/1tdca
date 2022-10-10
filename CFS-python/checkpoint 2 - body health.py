#!/usr/bin/env python3

#Descrição: Este Programa é capaz de prever se você terá um corpo saudável, normal ou estragado daqui 30 anos.
#Autor: Lucas Antenucci
#Licença: GPL V3
#Data 11/09/2022
#versao 1.0


from sklearn import tree

diariamente = 1
frequentemente = 2
dificilmente = 3

saudavel = 1 
normal = 2
estragado = 3

body_health = [[10,30, diariamente, diariamente, diariamente], [5,15,frequentemente,frequentemente,frequentemente], [4,6,dificilmente,dificilmente,dificilmente]]
resultados = [saudavel, normal, estragado]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(body_health, resultados)

print("Bem vindo ao seu body health anual, responda as perguntas em paramentros anuais para saber qual sera sua saude do corpo daqui 30 anos!\n")

print("O ano tem 8640 horas!\n")

atv_fisicas = input("Com qual frequencia anual em porcentagem voce pratica atividades fisicas? : ")
qualidade_sono = input("\nQual a sua porcentagem de horas de sono anual? : ")
comer_frutas = input("\nCom qual frequencia voce come frutas?, responda [1] - Diariamente , [2] - Frequentemente, [3] - Dificilmente : ")
refeicoes_dia = input("\nCom qual frequencia voce faz 3 refeicoes por dia?, responda [1] - Diariamente , [2] - Frequentemente, [3] - Dificilmente : ")
tomar_sol = input("\nCom qual frequencia voce toma sol?, responda [1] - Diariamente , [2] - Frequentemente, [3] - Dificilmente : ")

resultuser = clf.predict([[atv_fisicas, qualidade_sono, comer_frutas, refeicoes_dia, tomar_sol]])
print("\nResultados:")
if resultuser == 1:
    print("\nParabens! Daqui 30 anos voce tera um corpo saudavel, continue assim!")
elif resultuser == 2:
    print("\nSe esforce mais!, Daqui 30 anos voce tera um corpo normal, ta quase la!")
elif resultuser == 3:
    print("\nMude seus habitos! Daqui 30 anos voce tera um corpo estragado, mude imediatamente!")
