#!/usr/bin/env python3

from sklearn import tree

lisa = 1
irregular = 0
maca =1
laranja = 0

pomar = [[150, lisa], [130, lisa], [180, irregular], [160, irregular]]

resultado = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Por favor, digite o peso da fruta: ")
superficie = input("Por favor, informe a superficie (0)-irregular (1)-Lisa : ")

resultuser = clf.predict([[peso, superficie]])

if resultuser == 1:
    print("MACA")
else:
    print("LARANJA")