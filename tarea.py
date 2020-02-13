import msvcrt

if __name__ == "__main__":

print("Lista de mercado")

lista={}



#Abrir archivo para convertir sus lineas en keys



listilla=open("Lista.txt","r").read().split('\n')
5
for linea in listilla:

if linea in lista.keys():

lista[linea]+=1

else:

lista[linea]=1

#imprimir lista

for k,v in lista.items():

print(k,v)

#Pedir si quiere algo mas...

quiere=input("Quiere algo mas? Es todo...(Si o No)\nR/. ")

while quiere.lower()=="si":

nuevoproducto=input("\nDime si quieres algo mas... no tengo todo el día .\nR/. ")

if nuevoproducto in lista.keys():

lista[nuevoproducto]+=1

else:

lista[nuevoproducto]=1



quiere=input("\nQue mas? Es todo...(Si o no)\nR/. ")

#imprimir lista

for k,v in lista.items():

print(k,v)

#Quiere borrar algo

borrar=input("\nNo me digas que no puedes ni pensar bien\n Borraras algo?(Si o no)\nR/. ")

while borrar.lower()=="si":

borrarproducto=input("\nDime vas a borrar\nR/. ")

if borrarproducto in lista.keys():

lista[borrarproducto]-=1

if lista[borrarproducto]==0:

del lista[borrarproducto]

borrar=input("\nYa... lo demas si lo quieres?(Si o no)\nR/. ")

else:

print("\nTu no tienes cabeza o que? Eso no lo pusiste.")

#imprimir lista

for a,b in lista.items():

print(a,b)

#Sustituir

sustituto=input("\nY te pregunto...\nVas a cambiar algo?(Si o no)\nR/. ")

while sustituto.lower()=="si":

print("\nTodo bien??\n Que vas a cambiar??\n muevete")

cambio=input("\nR/. ")

if cambio in lista.keys():

del lista[cambio]



artcam=input("\n Que quieres agregar?? Rapido!!\nR/. ")

if artcam in lista.keys():

lista[artcam]+=1

else:

lista[artcam]=1

sustituto="no"

else:

print("\nSeguro? Eso no lo pusiste!!")





#imprimir lista

for a,b in lista.items():

print(a,b)

print("\nListo...")

print("Toma tu vaina... Chao")

listanueva=open("Lista.txt","a+")

for e in lista:

listanueva.write("\n"+e)

listanueva.close()

msvcrt.getch()
