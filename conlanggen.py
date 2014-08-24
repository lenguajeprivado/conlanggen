# -*- coding: utf-8 -*-

import random #módulo para el azar
import sys #este módulo lo usaré como sys.stdout en lugar de print para mantener las letras juntas
import time #módulo para agregar la fecha en el txt

#función que regresa a silaba[0]
def y():
        global g
        global x
        g = silaba[x]
        return g

#función que aumenta uno en silaba[x] para leer cada una de las letras de "silaba"
def yuno():
        global g
        global x
        x = (x+1)
        return x

#funcion que escribe los resultados al archivo txt
def archivo():
        global n
        file.write(n),


### Inicia el menú cuando se abre el programa
print """
+conlanggen  (v. 1.0)+
GENERADOR DE PALABRAS

-----Menú----
 1  - Generar lista de palabras
 2  - Ver instrucciones
 3  - Salir
"""
menu = input("¿Qué deseas hacer? [1,2,3]: ") #El usuario ingresa opciones de menú
if menu == 2:  #si elige la opción 2, muestra el texto
        print ("\n")
        print '''
        INSTRUCCIONES  
        
        Este pequeño programa genera listas de palabras 
        para utilizarlas en la creación de diccionarios de 
        lenguas artificiales (conlangs).
        
        Se utiliza de la siguiente manera:
        
        1. LETRAS A USAR
        
        1.1 Primero hay que llenar el campo de las vocales. 
        Al escribirlas hay que separar cada una con comas:
        
              Escribe las vocales [V]: a,e,i,o,u
        
        Se pueden utilizar signos sobre las vocales o
        vocales dobles: aa,ö,í
        
        1.2 Despues se llena el campo de las consonantes.
        También deben de ir separadas por comas. Se
        pueden agregar consonantes geminadas.
        
              Escribe las consonantes [C]: p,t,k,b,d,g,th,ff
        
        1.3 Existe la categoría "otros" la cual sirve para
        agregar letras características, sufijos o prefijos,
        apostrofes, aspiradas o cualquier cosa que queramos
        agregar. 

              Escribe sufijos o prefijos [T]: ado,ido,to,so,cho
                
        2. FONOTÁCTICAS
        
        2.1 El programa permite, de manera muy elemental,
        decidir cuales son las restricciones y la estructura 
        de cada una de nuestras palabras.
        
        2.2  Hay que usar siempre las mayúsculas para que
        funcione.
        
        2.3 Necesitamos agregar la forma en la quequeremos
        que cada palabra esté compuesta.
        Donde pongamos una C, irá una consonante.
        Donde pongamos una V, irá una vocal.
        Donde pongamos una T, aparecerán los sufijos y prefijos.
        
        2.4 Si queremos una palabra como "manzana" entonces
        la estructura será "CVCCVCV". Para la palabra "vaca" 
        sería "CVCV"
        Si asignamos en sufijos y prefijos [T]  la terminación 
        "-ido" y queremos una palabra como "comido" 
        entonces la estructura sería CVCVT.
        
        2.5 Hay que separar con comas cada una de las 
        estructuras.
        
        ¿Cuáles son las estructuras?: CV,CVC,TVC,CVCV,CCV,TVCV
        
        3. DETALLES
        
        3.1 Finalmente el programa preguntará cuántas palabras
        queremos generar en nuestra lista:
        
        ¿Cuántas palabras?: 25
        
        3.2 El programa mostrará las palabras generadas y 
        automáticamente creará un archivo llamado "palabras.txt"
        en la carpeta donde se encuentra este programa.
        Cada que se ejecuta el programa, sobreescribe este archivo
        así que debes asegurarte de copiar tus palabras si quieres
        generar una nueva lista.
        
        4. ACERCA DE
        
        conlanggen Ver. 1.0
        Generador de palabras.
        Creado por Daniel Martínez para el "Taller de lenguas
        artificiales" de la FQ, UNAM. México, 2014
        daniel.m.olivera@gmail.com
        tw: @jackeliand
        '''
        
        menu = input("[1  - Crear palabras]  [2  -  Salir] :") #Menú dentro de "instrucciones"
        if menu == 1:
                print " " #si elige 1, sólo escribe un espacio y sigue el programa
        else:
                quit()  #Con cualquier número que ponga, sale
elif menu == 3: #Con la opción 3, sale.
        quit()

###Termina el menú

### Inicia la parte principal del programa

#El usuario ingresa las letras. Se usa raw_input para que lea
#las cadenas como listas. .split(",") indica que divide la lista
#en las comas.
print "\n"
vocal = raw_input ("Escribe las vocales [V]:       ") .split (",")
conso = raw_input ("Escribe las consonantes [C]:   ") .split (",")
otros = raw_input ("Escribe sufijos o prefijos [T]:") .split (",")
print "\n"
modelos =  raw_input ("¿Cuáles son las estructuras? [C,V,T]:  ") .split (",")
print "\n"
#se agrega la variable "cont" para saber cuántas palabras generar
cont = int(input("¿Generar cuántas palabras? [1-200]:    "))

silaba = random.choice(modelos)
#Lee la variable "modelos" (las secuencias de palabras CVCVC), elige una al azar y la
#mete en la variable "silaba"
 
a = 0 #Este es el contador de cada una de las veces que crea una palabra
x = 0 
#Esta variable la uso para que lea cada uno de los caracteres de las cadenas
#dentro de "silaba" así: silaba[x]. En este caso, como está en cero
#lee la primera letra de la cadena que se haya elegido al azar.

#### Esto es para crear el archivo txt y su cabecera
file = open("palabras.txt", "w")
file.write("LISTA DE PALABRAS")
file.write("\n")
file.write("\n")
file.write (time.strftime("%d/%m/%Y")) ## dd/mm/yyyy format
file.write("\n")
file.write("\n")
####Fin de la cabecera del txt

while a < cont: #Esto es para cuántas veces queremos que repita el proceso (¿cuántas palabras?).
        for len in silaba: #Len dice el número de caracteres en una cadena. CVVC=4
                y() #Reset silaba[0]
                if g == "C":  #Donde haya una C, escoje una consonante al azar, la muestra y la escribe al txt
                        n = random.choice(conso)
                        sys.stdout.write(n)
                        archivo()
                elif g == "V":  #Donde haya una V, escoje una vocal al azar, la muestra y la escribe al txt
                        n = random.choice(vocal)
                        sys.stdout.write(n)
                        archivo()
                elif g == "T":  #Donde haya una T, escoje otra letra al azar, la muestra y la escribe al txt
                        n = random.choice(otros)
                        sys.stdout.write(n)
                        archivo()
                yuno() #silaba[+1] así lee cada una de las letras de "silaba"
        print "  "
        file.write("\n")
        a += 1 # Contador +1, una palabra más.
        x = 0 #Reset silaba[0]
        silaba = random.choice(modelos)  #Elige un nuevo modelo de palabra
        

file.close()  #cierra el txt

print "\n"
print 'Lista copiada a "palabras.txt".'  #frase de cierre
print "\n"

#Agosto 23, 2014
#Generador de palabras conlanggen Ver. 1.0
#twitter: @jackeliand
