import random
lista_de_numeros=list(range(100))#0-99
pares=[numero for numero in lista_de_numeros if numero % 2 == 0]#solo los pares

student_uid =[1,2,3]
studends=['rafa','pablo','sergip']
studends_with = {uid: student for uid, student in zip(student_uid, studends)}

random_numbers=list()

for i in range(10):
    random_numbers.append(random.randint(1,3))

mpm_repea={number for number in random_numbers}