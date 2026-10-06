'''
NOTAS:
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2. Es ver cuanto crece el numero de 
operaciones en mi algoritmo conforme
crece el tamaño de la entrada
Agrego las bigO identificadas
Teniendo en cuenta la Cota superior asintótica
O(n) + O(4) = O(n+4) = O(n)
'''
#creando una lista de estudiantes
student_list_01 = ["Juan", "Maria", "Pedro"]
student_list_02 = ["Ana", "Luis", "Carlos"]

#Verificar precencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # O(n)
            print("Estudiante encontrado👍") # O(1)
            return student #O(1)
    # si no encuentro al estudiante 
    print("Estudiante no encontrado😢") # O(1)
    return None # O(1)

#probando algoritmo
check_student("Juan", student_list_01)
