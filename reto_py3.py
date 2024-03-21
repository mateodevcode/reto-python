# Ejercicios de programación en Python

# 1. Crea un diccionario con los siguientes key-values: "Name": "Testing", "Age": 0

my_dict = {"Name": "Testing", "Age": 0}
print(my_dict)
# 2. Inserta en el diccionario que has creado el key-value: "Debug": False

my_dict["Debug"] = False
print(my_dict)

# 3. Muestra por pantalla el valor asociado al key "Debug"

print(my_dict["Debug"])

# 4. Inserta en el diccionario que has creado el key-value: "Lista": [[1, 2, 3], 100]

my_dict["Lista"] = [[1, 2, 3], 100]
print(my_dict)

# 5. Accede al último elemento del key "Lista"

print(my_dict["Lista"][-1])


# 6. Borra el key-value "Debug": False

del my_dict["Debug"]
print(my_dict)

# 7. Borra el key-value "Age": 0 y guarda el valor en una variable llamada valor


valor = my_dict.pop("Age")
print(valor)

# 8. Añade dentro de la lista dentro de la lista del key "Lista", el elemento -300

my_dict["Lista"][0].append(-300)
print(my_dict)