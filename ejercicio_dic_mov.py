import csv

fichero = open("data/movimientos.csv", "r")
reader = csv.reader(fichero)

print ("reader---->", reader)

lista_de_listas = []
dic_model = {}
lista_dict = []
lista_dict_2 = []

for lista in reader:
    lista_de_listas.append(lista)

for item in lista_de_listas[0]:
    dic_model[item] = ""
lista_de_listas.remove(lista_de_listas[0])

var = 0
v = 0
while var < len(dic_model):
    concepto = {}
    i = 0
    for key in dic_model:
        lista = [valor[i] for valor in lista_de_listas]  # valor x columnas
        concepto[key] = f"{lista[v * 1]}"
        i += 1
    v += 1
    var += 1
    lista_dict.append(concepto)

print("lista_dict ------>",lista_dict)
