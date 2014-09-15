# -*- coding: utf-8 -*-

instr = """

conlanggen 2.1
==========

Generador de palabras para conlangs




INSTRUCCIONES  
        
Este pequeño programa genera listas de palabras
para utilizarlas en la creación de diccionarios de
lenguas artificiales (conlangs).
        
Se utiliza de la siguiente manera:
        

1. LETRAS A USAR
        
1.1 Primero hay que llenar el campo de las vocales. 
Al escribirlas hay que separar cada una con comas:
        
Vocales [V]: a,e,i,o,u
        
Se pueden utilizar signos sobre las vocales o
vocales dobles: aa,ö,í
        
        
1.2 Después se llena el campo de las consonantes.
También deben de ir separadas por comas. Se
pueden agregar consonantes geminadas.
        
Consonantes [C]: p,t,k,b,d,g,th,ff
        
        
1.3 Existe la categoría "suf - pref" la cual sirve para
agregar letras características, sufijos o prefijos,
apostrofes, aspiradas, signos raros o cualquier cosa
que queramos agregar. 

Suf - Pref [T]: ado,ido,to,so,cho

o

Suf - Pref [T]: thy,gel,',u'h,m'hg



2. FONOTÁCTICAS
        
2.1 El programa permite, de manera muy elemental,
decidir cuales son las restricciones y la estructura 
de cada una de nuestras palabras.
        
2.2  Hay que usar siempre las MAYÚSCULAS para 
que funcione.
        
2.3 Necesitamos agregar la forma en la que 
queremos que cada palabra esté compuesta.
- Donde pongamos una C, irá una consonante.
- Donde pongamos una V, irá una vocal.
- Donde pongamos una T, aparecerán los sufijos y
prefijos.
        
2.4 Si queremos una palabra como "manzana" 
entonces la estructura será "CVCCVCV". Para la 
palabra "vaca" sería "CVCV".
Si asignamos en sufijos y prefijos [T]  la terminación 
"-ido" y queremos una palabra como "comido" 
entonces la estructura sería CVCVT.
        
2.5 Hay que separar con comas cada una de las 
estructuras.
        
Secuencias: CV,CVC,TVC,CVCV,CCV,TVCV
        


3. DETALLES
        
3.1 Finalmente el programa preguntará cuántas 
palabras queremos generar en nuestra lista:
        
Num. de palabras: 25
        
3.2 Al usar el botón de GENERAR, el programa nos 
entregará nuestra lista de palabras.

3.3 Si deseamos una copia, podemos usar el botón
"guardar en archivo .txt" lo cual creará un archivo 
llamado "palabras.txt" en la carpeta donde se 
encuentra el programa.
        
3.4 Cada que se aprieta el botón, sobreescribe este
archivo SIN AVISAR; así que debes asegurarte de
copiar tus palabras en otra carpeta si quieres
generar una nueva lista.
        
        
4. ACERCA DE
        
conlanggen Ver. 2.1
Generador de palabras.
(con GUI y fallos corregidos)

Creado por Daniel Martínez para el "Taller de lenguas
artificiales" de la FQ, UNAM. México, 2014
daniel.m.olivera@gmail.com
tw: @jackeliand
"""
