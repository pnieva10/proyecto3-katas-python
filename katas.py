# Proyecto 3 - Katas Python

from functools import reduce
import math


# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un
# diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben
# ser considerados.
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra == " ":
            continue
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

print(frecuencia_letras("hola mundo"))


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().
numeros = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, numeros)))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como
# parámetros. La función debe devolver una lista con todas las palabras de la lista
# original que contengan la palabra objetivo.
def palabras_con_objetivo(palabras, objetivo):
    resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado

print(palabras_con_objetivo(["casa", "casamiento", "perro"], "casa"))


# 4. Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

print(diferencia_listas([10, 20, 30], [1, 2, 3]))


# 5. Escribe una función que tome una lista de números como parámetro y un valor
# opcional nota_aprobado (por defecto 5). La función debe calcular la media de los
# números en la lista y determinar si la media es mayor o igual que nota_aprobado.
# Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe
# devolver una tupla que contenga la media y el estado.
def media_y_estado(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

print(media_y_estado([4, 6, 8]))


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# 7. Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().
def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

print(tuplas_a_strings([(1, 2), ("a", "b")]))


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el
# usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas
# excepciones de manera adecuada y muestra un mensaje indicando si la división fue
# exitosa o no.
try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    resultado = numero1 / numero2
except ValueError:
    print("Error: no has introducido un número. La división no se ha realizado.")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero. La división no se ha realizado.")
else:
    print(f"División realizada con éxito. Resultado: {resultado}")


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y
# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista
# de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter().
def mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))

print(mascotas_permitidas(["Perro", "Tigre", "Gato", "Oso"]))


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la
# lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio_lista(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("La lista está vacía.")
    return sum(numeros) / len(numeros)

try:
    print(promedio_lista([]))
except ListaVaciaError as error:
    print(f"Error: {error}")


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario
# ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor
# que 0 o mayor que 120), maneja las excepciones adecuadamente.
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("la edad debe estar entre 0 y 120")
    print(f"Tu edad es {edad}")
except ValueError as error:
    print(f"Edad no válida: {error}")


# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud
# de cada palabra. Usa la función map().
def longitud_palabras(frase):
    return list(map(len, frase.split()))

print(longitud_palabras("Me gusta Python"))


# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de
# tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar
# repetidas. Usa la función map().
def mayusculas_minusculas(caracteres):
    letras = set(caracteres.lower())
    return list(map(lambda letra: (letra.upper(), letra), letras))

print(mayusculas_minusculas("abBa"))


# 14. Crea una función que retorne las palabras de una lista que comiencen con una
# letra en específico. Usa la función filter().
def empiezan_por(palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))

print(empiezan_por(["manzana", "pera", "melón"], "m"))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
print(sumar_tres([1, 2, 3]))


# 16. Escribe una función que tome una cadena de texto y un número entero n como
# parámetros y devuelva una lista de todas las palabras que sean más largas que n.
# Usa la función filter().
def palabras_mas_largas(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))

print(palabras_mas_largas("El curso de Python", 3))


# 17. Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
def digitos_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

print(digitos_a_numero([5, 7, 2]))


# 18. Escribe un programa en Python que cree una lista de diccionarios con información
# de estudiantes (nombre, edad, calificación) y use filter para extraer a los
# estudiantes con una calificación mayor o igual a 90.
estudiantes = [
    {"nombre": "Ana", "edad": 22, "calificacion": 95},
    {"nombre": "Luis", "edad": 25, "calificacion": 78},
    {"nombre": "Marta", "edad": 21, "calificacion": 90},
]
print(list(filter(lambda e: e["calificacion"] >= 90, estudiantes)))


# 19. Crea una función lambda que filtre los números impares de una lista dada.
impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
print(impares([1, 2, 3, 4, 5]))


# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista
# solo con los valores int. Usa la función filter().
lista_mixta = [1, "dos", 3, "cuatro"]
print(list(filter(lambda x: type(x) == int, lista_mixta)))


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
cubo = lambda x: x ** 3
print(cubo(3))


# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
print(reduce(lambda x, y: x * y, [2, 3, 4]))


# 23. Concatena una lista de palabras. Usa la función reduce().
print(reduce(lambda x, y: x + y, ["Hola", " ", "mundo"]))


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
print(reduce(lambda x, y: x - y, [100, 20, 10]))


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("Python"))


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda x, y: x % y
print(resto(10, 3))


# 27. Crea una función que calcule el promedio de una lista de números.
def promedio(numeros):
    return sum(numeros) / len(numeros)

print(promedio([10, 20, 30]))


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = []
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)

print(primer_duplicado([3, 5, 1, 5, 3]))


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare
# todos los caracteres con el carácter '#' excepto los últimos cuatro.
def enmascarar(variable):
    texto = str(variable)
    return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarar(123456789))


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están
# formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(son_anagramas("Roma", "amor"))


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego
# un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje
# indicando que fue encontrado; de lo contrario, lanza una excepción.
def buscar_nombre():
    nombres = input("Introduce nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre = input("Nombre a buscar: ").strip()
    if nombre in nombres:
        print(f"{nombre} ha sido encontrado.")
    else:
        raise ValueError(f"{nombre} no está en la lista.")

try:
    buscar_nombre()
except ValueError as error:
    print(f"Error: {error}")


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el
# nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo
# contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {"nombre": "Laura García", "puesto": "Analista"},
    {"nombre": "Carlos Pérez", "puesto": "Desarrollador"},
]
print(buscar_puesto("Carlos Pérez", empleados))
print(buscar_puesto("Juan Martín", empleados))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))
print(sumar_listas([1, 2, 3], [10, 20, 30]))


# 34. Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
#   Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#   Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#   Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#   Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#   Implementar el método quitar_rama para eliminar una rama en una posición específica.
#   Implementar el método info_arbol para devolver información sobre la longitud del tronco,
#   el número de ramas y sus longitudes.
# Caso de uso:
#   a. Crear un árbol.
#   b. Hacer crecer el tronco una unidad.
#   c. Añadir una nueva rama.
#   d. Hacer crecer todas las ramas una unidad.
#   e. Añadir dos nuevas ramas.
#   f. Retirar la rama situada en la posición 2.
#   g. Obtener información sobre el árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def info_arbol(self):
        return f"Tronco: {self.tronco}, número de ramas: {len(self.ramas)}, longitudes: {self.ramas}"

arbol = Arbol()           # a
arbol.crecer_tronco()     # b
arbol.nueva_rama()        # c
arbol.crecer_ramas()      # d
arbol.nueva_rama()        # e
arbol.nueva_rama()
arbol.quitar_rama(2)      # f
print(arbol.info_arbol()) # g


# 35. Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
#   Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
#   Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
#   Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
#   Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
#   a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50,
#      ambos con cuenta corriente.
#   b. Agregar 20 unidades al saldo de Bob.
#   c. Transferir 80 unidades de Bob a Alicia.
#   d. Retirar 50 unidades del saldo de Alicia.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)  # a
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)                      # b
try:
    alicia.transferir_dinero(bob, 80)       # c
except ValueError as error:
    print(f"Error: {error}")
alicia.retirar_dinero(50)                   # d
print(f"Alicia: {alicia.saldo}, Bob: {bob.saldo}")


# 36. Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
#   Crear una función contar_palabras que cuente el número de veces que aparece cada palabra
#   en el texto y devuelva un diccionario.
#   Crear una función reemplazar_palabras para sustituir una palabra_original por una
#   palabra_nueva en el texto y devolver el texto modificado.
#   Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
#   Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar",
#   "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
#   Verificar el funcionamiento completo de procesar_texto.
def contar_palabras(texto):
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = [p for p in texto.split() if p != palabra]
    return " ".join(palabras)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        return "Opción no válida"

texto = "el gato y el perro"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "gato", "loro"))
print(procesar_texto(texto, "eliminar", "el"))


# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la
# hora proporcionada por el usuario.
hora = int(input("Introduce la hora (0-23): "))
if 6 <= hora < 14:
    print("Es de día")
elif 14 <= hora < 21:
    print("Es de tarde")
else:
    print("Es de noche")


# 38. Escribe un programa que determine qué calificación en texto tiene un alumno
# según su calificación numérica.
# Reglas:
#   0 - 69: insuficiente
#   70 - 79: bien
#   80 - 89: muy bien
#   90 - 100: excelente
nota = int(input("Introduce la calificación (0-100): "))
if nota <= 69:
    print("Insuficiente")
elif nota <= 79:
    print("Bien")
elif nota <= 89:
    print("Muy bien")
else:
    print("Excelente")


# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser
# "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios
# para calcular el área de la figura).
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return base * altura / 2

print(calcular_area("rectangulo", (4, 5)))
print(calcular_area("circulo", (3,)))
print(calcular_area("triangulo", (6, 4)))


# 40. Escribe un programa en Python que utilice condicionales para determinar el monto
# final de una compra en una tienda en línea, después de aplicar un descuento.
# El programa debe:
#   a. Solicitar al usuario el precio original de un artículo.
#   b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#   c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#   d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#   e. Mostrar el precio final de la compra, considerando o no el descuento.
#   f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
precio = float(input("Precio original: "))
respuesta = input("¿Tienes cupón de descuento? (sí/no): ").lower()

if respuesta == "sí" or respuesta == "si":
    cupon = float(input("Valor del cupón: "))
    if cupon > 0:
        precio = precio - cupon
    else:
        print("Cupón no válido")
elif respuesta != "no":
    print("Respuesta no válida")

print(f"Precio final: {precio}")
