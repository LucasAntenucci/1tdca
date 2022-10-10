from unittest import result
from sklearn import tree

casapequena = 0
casamedia = 1
casagrande = 2


resultado = [[70], [120], [160]]
tamanho = [[casapequena], [casamedia], [casagrande]]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(resultado, tamanho)

metros = int(input("Por favor, digite a metragem da casa: "))
#categoria = input("Por favor, informe a categoria (0)-casa pequena (1)-casa media (2)-casa grande : ")

valor = 1000 * metros



resultuser = clf.predict([[metros]])

if resultuser == 0 :
    print("A casa é pequena")
    print("O valor da casa é : R$ {} ".format(valor))
elif resultuser == 1:
    print ("casa media")
    print("O valor da casa é : R$ {} ".format(valor))
elif resultuser == 2:
    print("casa grande")
    print("O valor da casa é : R$ {} ".format(valor))



