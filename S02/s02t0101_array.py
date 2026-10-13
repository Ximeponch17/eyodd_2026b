#Array
#from array import +
import array as arr

#creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero Decimal
# d: Numero decimal doble
# u: Caracter Unicode
my_array = arr.array('i', [10,20,300,3,7,40,55,88,700,3,11])

# Intencion automatica
# for num in my_array: 
    # print(num)

# Acceso inidividual a los elementos 
# print(my_array[0])# Primer elemento 
# print(my_array[1])# Segundo elemento
# print(my_array[2])# Tercer elemento

# Tamaño de un arreglo 
# Length
# print(len(my_array))

# Interacion por indice
#for i in range(len(my_array)):
    #if my_array[i] % 2 == 0:
     #print(f"Elemento Num {i+1}: {my_array[i]}")

#Busqueda de un elemento 
num_to_search = 200

#Modificando un valor
#backet notation
my_array[7] = 200

try:
    print(f"Localizando {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("⚠Numero no encontrado!!!")

#Asignando valor en un indice que no existe
try:
    my_array[100] = 3
except:
    print("⚠Indice fuera de rango!!!")