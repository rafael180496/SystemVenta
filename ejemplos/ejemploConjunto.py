
from sympy import FiniteSet
"""
------ TUPLAS ------
Las tuplas (tuples) son similares a las listas.
La unica diferencia es que las tuplas son inmutables.
La diferencia con los strings es que pueden recibir muchos tipos valores.
Son una serie de valores separados por comas, casi siempre se le agregan
paréntesis para que sea mucho más legible.
tup = 1,2,3
tup = (1,2,3)-->Esta opción es la más se utiliza

Para poderla inicializar utilizamos la función 'tuple'.
Un uso muy común es utilizarlas para regresar más de
un valor en una función.
return (students,teachers)

------ CONJUNTOS ------
Los conjuntos (sets) son una colección sin orden que no 
permite elementos duplicados. A diferencia de los tuples podemos
agregar y eliminar, son mutables.
Los sets se inicializan con la función 'set'.
Para añadir elementos utilizamos el método 'add' y para eliminarlos
utilizamos el método 'remove'
"""

## LISTA --> ages = [12,18,24,34,50]
## TUPLA --> ages = (12,18,24,34,50)
## CONJUNTOS --> ages = {12,18,24,34,50}

"""Con las tuplas que pueden utilizar casi todas las (las mismas)
funciones y métodos que funcionan con las listas"""

##------ TUPLAS ------
a = (1, 2, 2, 3)
b = (3, 4, 5)
c = b+a
print(c)

print(a.count(2))  # Nos dice cuantas veces aparece el numero 2 en la tupla
# NOs dice en que posición aparece por primera el numero 4 en la tupla
print(b.index(4))

##Esto no lo podemos hacer porque son inmutables, al contrario que las listas, que son mutables
##a[1]= 10
##c[2] = 22

##------ CONJUNTOS ------
# Creando un conjunto en python
print('-'*30)
A = {1, 2, 3}
print(A)

# Creando un conjunto a partir de una lista
print('-'*30)
lista = ["bananas", "manzanas", "naranjas", "limones"]
B = set(lista)
print(B)

# Los conjuntos eliminan los elementos duplicados
print('-'*30)
lista = ["bananas", "manzanas", "naranjas", "limones",
         "bananas", "bananas", "limones", "naranjas"]
B = set(lista)
print(B)

# Creando el conjunto vacío
print('-'*30)
C = set()
print(C)

# Cardinalidad de un conjunto con len().
print('-'*30)
print("La cardinalidad del conjunto A = {0} es {1}".format(A, len(A)))

# comprobando membresía
print('-'*30)
print(2 in A)
print(0 in A)

# Igualdad entre conjuntos. El orden de los elementos no importa.
print('-'*30)
A = {1, 2, 3, 4}
B = {4, 2, 3, 1}
print(A == B)

# Subconjunto. No hay distincion entre subconjunto y propio
# para el conjunto por defecto de python.
print('-'*30)
A = {1, 2, 3}
B = {1, 2, 4, 3, 5}
"""issubset() busca si los valores de A están en B, sin importar el orden"""
print(A.issubset(B))

# Union de conjuntos. Omite los valores repetidos
print('-'*30)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
print(A.union(B))

# Intersección de conjuntos, es decir, los valores que se repiten
print('-'*30)
print(A.intersection(B))

# Diferencia entre conjuntos
print('-'*30)
print(A.difference(B))
print(B.difference(A))
print(A - B)
print(B - A)

##------ Utilizando sympy -------
# Utilizando FiniteSet de sympy
"""Para que el import no de error, abrir el power shell como admin
en la carpeta donde este el archivo (en mi caso, que utilizo el 
sublime text 3) o si ejecutais desde el interprete por consola, en ambos
casos teneis que poner pip install sympy"""
print('-'*30)
C = FiniteSet(1, 2, 3)
print(C)

# Generando el conjunto potencia. Esto no se puede
# hacer utilizando el conjunto por defecto de python.
print('-'*30)
print(C.powerset())

# Cardinalidad
print('-'*30)
print("La cardinalidad del conjunto potencia del conjunto C = {0} es {1}".
      format(C, len(C.powerset())))

# Igualdad
print('-'*30)
A = FiniteSet(1, 2, 3)
B = FiniteSet(1, 3, 2)
print(A == B)

A = FiniteSet(1, 2, 3)
B = FiniteSet(1, 3, 4)
print(A == B)

# Subconjunto y subconjunto propio
print('-'*30)
A = FiniteSet(1, 2, 3)
B = FiniteSet(1, 2, 3, 4, 5)
print(A.is_subset(B))

# A == B. El test de subconjunto propio da falso
print('-'*30)
B = FiniteSet(2, 1, 3)
print(A.is_proper_subset(B))

# Union de dos conjuntos
print('-'*30)
A = FiniteSet(1, 2, 3)
B = FiniteSet(2, 4, 6)
print(A.union(B))

# Interseccion de dos conjuntos
print('-'*30)
A = FiniteSet(1, 2)
B = FiniteSet(2, 3)
print(A.intersect(B))

# Diferencia entre conjuntos
print('-'*30)
print(A - B)

# Calculando el producto cartesiano. Con el conjunto por
# defecto de python no podemos hacer esto con el operador *
print('-'*30)
A = FiniteSet(1, 2)
B = FiniteSet(3, 4)
P = A * B
print(P)

for elem in P:
    print(elem)

# Elevar a la n potencia un conjunto. Calcula el n
# producto cartesiano del mismo conjunto.
print('-'*30)
A = FiniteSet(1, 2, 3, 4)
P2 = A ** 2
print(P2)

P3 = A ** 3
print(P3)

for elem in P3:
    print(elem)

