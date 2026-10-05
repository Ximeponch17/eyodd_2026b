import time

#crear la variable para el problema
n = 100
the_sum = 0

#toma el tiempo 1
timestamp_01 = time.time()
#iniciando la suma
while n > 0:
    the_sum += n
    n -= 1

#toma el tiempo 2
timestamp_02 = time.time()

#imprime la solucion
print(f"La suma es:, {the_sum}")

#calculamos el tiempo
elapsed_time = round((timestamp_02 - timestamp_01) * 1e6,2)

print(f"Tiempo de ejecucion: {elapsed_time} μs")
