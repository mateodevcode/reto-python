# Ejercicios de programación en Python

# 1. Crea una variable que contenga una lista con los siguientes elementos: "Cherry", "Berry", "Mango"

miLista = ["Cherry", "Berry", "Mango"]

# 2. Printa por pantalla la lista que has creado

print(miLista)

# 3. Añade a la lista que has creado en el punto 1 de este ejercicio, el entero 99 al final de la misma

miLista.append(99)
print(miLista)

# 4. Printa por pantalla el segundo elemento de esta lista

print(miLista[1])

# 5. Cambia el primer elemento de esta lista por otra lista vacía

miLista[0] = []
print(miLista)

# 6. Accede al primer elemento de esta lista (el cual es una lista) y añade dentro de esta lista el valor -100

miLista[0].append(-100)
print(miLista)

# 7. Borra el último elemento de la lista

miLista.pop()
print(miLista)

# 8. Inserta en la posición cero de la lista el valor decimal 3.141516

miLista.insert(0, 3.141516)
print(miLista)

# 9. Printa la lista dada la vuelta, desde atrás hacia adelante.

miLista.reverse()
print(miLista)
# 10. Borra el elemento "Berry" de la lista

miLista.remove("Berry")
print(miLista)