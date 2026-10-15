#Importando funcion Array
#del modulo array y renombrando
#como arr

from array import array as arr

#Importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i', [5,10,15,20])

print("---ANTES DE LA INSERCION---")
print_array(my_array)

# Insercion
my_array.insert(1, 90) 
print("---DESPUES DE LA INSERCION---")
print_array(my_array)

print ("---DESPUES DEL APPEND---")
my_array.append(1000)
print_array(my_array)

print("---SIMULAR UN APPEND CON INSERT---")
my_array.insert(len(my_array), 9000)
print_array(my_array)
