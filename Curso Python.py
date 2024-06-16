""" 
Este es un curso python para principiantes 
"""


#esto es un comentario, es decir no lo va a correr el programa

#variables de datos pueden ser de varios formatos
#STR (string) se usa para palabras y van entre ¨comillas¨
saludo = "hola mundo"
print(saludo)

#INT o numeros enteros
edad=42
print(edad)

#FLOAT es para numeros decimales
PI = 3,14159
print(PI)

#Valor (BOOL) BOOLEANO  True or False
valor_booleano=True

#Palabras reservadas de Python
import keyword
print(keyword.kwlist)

#las constantes se escriben en mayusculas
NUMERO_PRECISO= 1234567890
print(NUMERO_PRECISO)

#operadores aritmeticos: suma, resta, multiplicación y división
#print operacion, sin variables
print(20 + 50)

#operador de suma o adición
numero1 = 10
numero2 = 20
print(numero1 + numero2)

#operador de resta o sustraccion
numero3 = 3
numero4 = 2
operacion = numero3-numero4
print(operacion)

#operador de multiplicacion
operacion=10*2 
print(operacion)

#operador de division
operacion=10/2
print(operacion)

#operadores diferentes
operacion=100*98+65*2-10/5
print(operacion)

"""operador de modulo, es como la division pero en vez
de darnos el resultado, nos da el resto de la division.

Dividendo es el numero que vamos a dividir
Divisor es el numero por el que vamos a dividir
Cociente es el resultado
Resto es el numero que queda de residuo en la division
"""
operacionA=10/3
operacionB=10%3
operacionC=10//3

print(operacionA, operacionB, operacionC)

#operador de potencias
operacion=2**3
print(operacion)

#operador con prioridad de calculo, esto se hace con parentesis
operacionA=10+6*2 #22
operacionB=(10+6)*2 #32
print(operacionA) 
print(operacionB)

#se puede usar "_" para separar sin que python lo interprete

variable=123_456_789
print(variable)



"""Concatenacion basica
Es la forma de unir o mejor dicho de añadir un string
 a otro"""
frase1="soñando que estamos despiertos, "
frase2="seguimos durmiendo."
frase_completa=frase1+frase2

print(frase_completa)


#Print (objects,sep,end, file, flush)
print("el resultado,de sumar",10, "mas", 50,"es",60)

#cuando lo ejecutamos nos aparece en consola: 
"""#"el resultado de sumar 10 mas 50 es 60"
como vemos ha hecho una concatenacion y puesto 
los espacios donde corresponde"""

#La funcion input se usa para ingresar datos.
nombre=input("ingresa tu nombre:")

"""en consola nos aprecera ingresa tu nombre y podremos 
escribir nuestros datos en este caso el nombre, que se 
guardara en sistema comop un str."""


print(nombre)

# \n de esta forma agregamos un salto de linea


#Introduccion a las listas
"""Las listas se usan para almacenar una coleccion ordenada
de elementos. pueden ser numeros, str, booleanos e incluso
otras listas"""

color="rojo"
talla="L"
precio=100
cantidad=10
 
camiseta=["rojo","L",100,10]
#en este print nos tira error porque no se puede concatenar un str con una list
# print("esta es una lista" + camiseta)
#la solucion es no concatenar y separar en el print el str de la list por una ,

print("esta es una list",camiseta)


#Formateo de str es incrustar valores en las cadenas de caracteres
#No es la accion de concatenar, pero el proposito es muy parecido
#la sintaxis es f¨¨

nombre=input("Por favor, introduzca su nombre.")

print(f"Hola, {nombre}, que tenga buen dia.")
print("Hola, " + nombre + ", que tenga un buen dia.")

#como usar distintas comillas
"""ej si tenemos que hacer un str donde el texto
lleva comillas ya sea dobles o simples, lo que 
debemos hacer es usar las otras comillas para
resaltar el str"""

print('"era un lujo" me dijo')

#Las list tienen indice de posicion
#A cada elemento de la list se le asigna un numero
#Empezando siempre por 0,1,2,3,4,5,etc.
#Se puede cambiar los elementos temporalmente por posicion

colores=["azul","amarillo","rojo"]
colores[0]="verde"
print(colores) 

#Con el method append podcremos agregar un elemento a la list
#Este elemento se agregara al final de la list
colores=["rojo","verde","azul"]
colores.append("amarillo")
print(colores)

"""#Con el method insert podremos agregar un elemento a la list 
en la posicion que querramos"""

colores=["rojo","verde","amarillo"]
colores.insert(0,"azul")
print(colores)
 
"""#El method extend sirve para extender una list
 con un elemento o varios iterables"""

colores1=["rojo","azul","verde"]
colores2=["amarillo","violeta","naranja"]
colores1.extend(colores2)
print(colores1)

#El method pop se usa para eliminar elementos de una list
#Entre los () vamos a poner la posicion que queremos eliminar
colores=["rojo","verde","azul"]
colores.pop(1)
print(colores)

#El method remove sirve para eliminar elementos de una list
#Entre los() pondremos el valor literal, no la posicion
#En caso de que un elemento este repetido no borrara todos solo el primero

colores=["rojo","verde","azul"]
colores.remove("verde")
print(colores)

#El method index se usa para buscar un elemento en la list
#Nos arrojara como resultado el numero de la posicion en la que esta
#Si el elemento se repite en la list solo nos dira la posicion del primer elemento que aparezca

colores=["rojo","amarillo","verde"]
busca_color=colores.index("amarillo")
print(busca_color)

#El method count tambien busca elementos en la list
#Pero nos dira cuantas veces aparece en la list

numeros=[1, 10, 80, 10, 56, 10]
valor_busqueda=10 
coincidencias = numeros.count(valor_busqueda)
print(coincidencias)




"""#Constantes son contenedores de elementos, pero
a diferencia de las variables estas no pueden cambiarse,
es decir son constantes"""
#las CONSTANTES se escriben en mayusculas (es una convencion de python)
#en realidad no existen las constantes en python
#todas son variables es decir una constante la podriamos cambiar si quisieramos
#es por eso que se hizo la convencion, si esta en mayuscula no se cambia

NUMERO_CONSTANTE = 10
numero_variable = 10

#ejemplo de variables nombre edad temperatura telefono, etc
#ejemplo de constantes NUMERO_PI VELOCIDAD_DE_LA_LUZ  GRAVEDAD



#TUPLAS son una coleccion inmutable de elementos
#Las list son coleccion de variables
#Las tuplas son coleccion de constantes
#la sintaxis a diferencia de las list se usan los ()

tupla = ("rojo", "verde", "azul", "rojo")

#para seleccionar un elemento de la tupla se hace asi
#podremos el indice de posicion del elemento entre []
print(tupla[1])

#no se puede usar el method pop para borrar un elemento
#ya que son iunmutables no se borran o se cambian

#si se pueden usar method de lectura
#method index
print(tupla.index("rojo"))
#method  count
print(tupla.count("rojo"))



#sets son como las list pero no se pueden reasignar los elementos
#se pueden borrar o agregar elementos, pero no cambiar
#se pueden usar todos los elementos que sean inmutables
#los elementos de los sets son aleatorios, 
# es decir yo los escribo con un orden pero a la hora de ejecutarse 
# van air cambiando de posicion
#el method add se usa para agregar elementos a los set
#el method remove se usa para eliminar un elemento
#el method discard es para descartar elementos

set_colores = {"rojo", "verde", "zapallo"}
set_colores.add("azul")
set_colores.remove("zapallo")
set_colores.discard("azul")

print(set_colores)


#Method of str

#Method capitalize se usa para convertir en mayuscula la primer letra del str

frase = "el fin de la sociedad, tal como la conocemos"
frase_capitalize = frase.capitalize()

print(frase_capitalize)

nombre = input("Introduzca su nombre:\n")

saludo = "Hola, " + nombre.capitalize()

print(saludo)

#Method upper se usa para convertir toda la frase de str en mayuscula
frase = "el fin de la sociedad, tal como la conocemos"
frase_upper = frase.upper()

print(frase_upper)

#Method lower es para pasar a minusculas toda la frase del str
frase = "PASA TODO A MINUSCULAS"
frase_lower = frase.lower()

print(frase_lower)


#intro a los diccionarios
#son como las listas o las duplas, pero en vez de guardar posiciones numericas,
#guardan keys (claves) y values (valores)


#diccionario_o_dict = {"clave1" : "valor1", "clave2" : "valor2", "clave3", "valor3", ...}

camiseta = { "color" : "rojo", "talle" : "L", "precio" : "100", "unidades" : "10", }

#llamar a valor de diccionario
#se usan [] para llamar el valor

dato_obtenido = camiseta["color"]

print(dato_obtenido)

#comprobar stock
print(f"hay {camiseta ["unidades"]} unidades en el almacen")

#modificar un valor

camiseta["unidades"] = 25

print(f"hay {camiseta ["unidades"]} unidades en el almacen actualizado")

# crear un nuevo atributo al diccionario

camiseta["marca"] = "Adidass"

print(camiseta)


#eliminar una clave del diccionario

del camiseta["precio"]

print(camiseta)

#para borrar un diccionario tambien se usa del

# del camiseta
#print(camiseta)



#casting o conversion, implicita o explicita.

#se puede usar para transformar un str en un int o float

#para operar conversiones de tipos de datos tenemos

#las funciones predefinidas in, str, full, list, apple,

#  dict, set, hex, bin, oct.

#conversion implicita
numero1 = 10  #int
numero2 = 20.5 #float

print(numero1 + numero2) #solo python lo pasa a float

#con el comando "type" veremos la clase de la variable o lo que queremos ver
print(type(numero1 + numero2))
#nos devuelve en pantalla <class 'float'>


#conversion explicita, es aquella que debemos indicarle a python
#que la haga, es decir no la realiza automaticamente

numero1 = 10
numero2 = 20.5
print(numero1 + int (numero2))
#nos devuelve un resulñtado en enteros (30) aunque hubiese un float.

numero_1 = input("introduzca el primer numero: ")
numero_2 = input("introduzca el segundo numero: ")

numero_1 = int(numero_1) #sino hacemos esta conversion en vez de
numero_2 = int(numero_2) #una operacion aritmetica, nos hara una concatenacion
                         # de str
    suma = numero_1 + numero_2

print(f"tipo de numero_1: {type(numero_1)}")
print(f"tipo de numero_2: {type(numero_2)}")




print(f"el resultado de la suma es: {suma}.")


#otra forma de hacer una conversion seria
numero_1 = int(input("introduzca el primer numero: "))
numero_2 = int(input("introduzca el segundo numero: "))

print(f"el resultado de la suma es: {suma}")








































































