# Ejercicios de programación en Python

# 1. Printa por pantalla el string "Hello World!"

print("Hello World!")

# 2. Printa por pantalla el string "La mente no es un vaso que llenar sino una lámpara que encender"

print("La mente no es un vaso que llenar sino una lámpara que encender")

# 3. Printa por pantalla la primera letra del string "The Bridge"

print("The Bridge"[0])

# 4. Printa el string "Hello World!" desde atrás hacia adelante

print("Hello World!"[::-1])


# 5. Printa desdel caracter dos hasta el caracter seis (incluido) del string "Be water my friend"

print("Be water my friend"[2:7])

# 6. Crea una variable con el string "No puedes bañarte dos veces en el mismo río" y muéstralo por pantalla con todas sus letras en mayúsculas

variable_1 = "No puedes bañarte dos veces en el mismo río"
print(variable_1.upper())

# 7. Pasa el string "HELLO WORLD!" a minúsculas

print("HELLO WORLD!".lower())

# 8. Printa el string "   Tengo espacions   " sin los espacios al principio y al final

print("   Tengo espacios   ".strip())

# 9. Printa el string "Tengo varios espacios" en forma de lista separado por los espacios, donde cada elemento de la lista es una palabra

print("Tengo varios espacios".split())

# 10. Crea una variable con el string "The Bridge". Tras esto cambia el primer caracter de esta variable por una "Q"

variable_2 = "The Bridge"
variable_2 = "Q" + variable_2[1:]
print(variable_2)

# 11. Muéstra por pantalla el tipo de la variable que has creado en el punto 10 de este ejercicio

print(type(variable_2))