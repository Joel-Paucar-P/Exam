#CASO: Elaborar el código de la multiplicación de una matriz bidimensional, 
#utilizar funciones para realizar la operación multiplicación. 
#Asimismo, el resultado ordenar de manera descendente. 
#Finalmente, realizar una función de búsqueda para revisar si la matriz resultado tiene el valor 9, 
#en caso fuese afirmativo, indicar por pantalla " La matriz tiene el valor 9 y se encuentra en la 
#posición i (fila) y j (columna).

n=int(input("Determinar el numero de filas: "))
lista=[]
for i in range(n):
    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    lista.append(x)
print(lista)
print("\n")
for i in range(n):
    for j in range(len(x)):
        if lista[i][j]==9:
            print(f"El numero 9 esta ubicado en la fila {i+1} y en la columna {j+1}")
print("\n")
nuv=[]
for i in range(n):
    valor=0
    for j in range(len(x)):
        valor=int(valor)
        multi=lista[i][j]*lista[j][i]
        valor=valor+multi
    valor=str(valor)
    var=valor.split()
    nuv.append(var)
print(nuv)