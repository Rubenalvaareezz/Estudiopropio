curso_actual = 1.5
curso_minimo = 2.5
curso_promedio = 4
curso_mas_lento = 7
#APARTADO A
print("------------------")
print("El curso de dalto dura: ")
diferencia1 = 100-(curso_actual * 1000 // curso_minimo)/10
print(f' -Un {diferencia1} % menos que el curso minimo')

diferencia2 = 100-(curso_actual *1000 // curso_mas_lento) / 10
print(f' -Un {diferencia2} % menos que el curso más lento')

diferencia3 = 100 - (curso_actual * 1000 // curso_promedio) / 10
print(f' -Un {diferencia3} % menos que el curso promedio')
print("------------------")

#APARTADO B

curso_crudo_acrual = 3.5
curso_crudo_promedio = 5

porcentaje_reducido_1 = 100-(curso_actual *1000 // curso_crudo_acrual)/10
print(f'El porcentaje que se reudce al editar en el curso de dalto es de un {porcentaje_reducido_1} %')

porcentaje_reducido_2 = 100-(curso_promedio *1000 // curso_crudo_promedio)/10
print(f'El porcentaje que se reudce al editar en un curso promedio es de un {porcentaje_reducido_2} %')
print("-----------------")

#APARTADO C

print(f'ver 10 horas del curso de dalto equivale a ver {(curso_promedio * 100 // curso_actual) / 10} horas de otros cursos')

print(f'ver 10 de otros cursos equivale a ver {curso_actual * 100 // curso_promedio / 10} horas del curso de dalto')
print("-----------------")