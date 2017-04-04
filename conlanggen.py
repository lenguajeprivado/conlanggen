# -*- coding: utf-8 -*-


### Recuerda que no sé nada de programación, por eso todo está feo.
### Si encuentras fallos, dime para corregirlos o hazlo por tu cuenta
### Sientete libre de usar lo que te sea útil o modificar todo mi programa.
### Recuerda darme un poquito de crédito cuando lo hagas.

from Tkinter import *   #traemos tkinter, un GUI para python
from info import instr   #importo el archivo de texto para las instrucciones
import random #módulo para el azar
import sys #este módulo lo usaré como sys.stdout en lugar de print para mantener las letras juntas
import time #módulo para agregar la fecha en el txt
import codecs  #como hubo problemas para escribir el archivo en utf-8, uso este módulo


###----------- esta clase servirá para dirigir el ouput hacia la textbox
class StdoutRedirector(object):
    def __init__(self, text_area):
        self.text_area = text_area
    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)
###--------- ouput ->textbox


#####------ ESTE ES EL PROGRAMA PRINCIPAL
def motor():
        global a
        global x
        a = 0
        x = 0
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
        #Con esto obtenemos el texto desde las entry. Cada una es dividida por las comas que ponga el usuario.
        vocal1 = e1.get()
        vocal1.split(",")
        vocal2 = e2.get()
        vocal2.split(",")
        conso1 = e3.get()
        conso1.split(",")
        conso2 = e4.get()
        conso2.split(",")
        sufijos = e5.get()
        sufijos.split(",")
        prefijos = e6.get()
        prefijos.split(",")
        extra = e7.get()
        extra.split(",")

        resultados.delete("1.0", END) #borro el textbox principal para que allí aparezcan las palabras
        resultados.config(foreground="black") #cambio el color del texto de la textbox a negro 
        
        modelos = sec.get('0.0', 'end')
        #modelos.split(",")
        cont = int(numm.get())
        silaba = random.choice(modelos.split(","))
        
        while a < cont: #Esto es para cuántas veces queremos que repita el proceso (¿cuántas palabras?).
                for len in silaba: #Len dice el número de caracteres en una cadena. CVVC=4
                        y() #Reset silaba[0]
                        if g == "V":  #Donde haya una V, escoje una letra al azar, la muestra y la escribe al txt
                                n = random.choice(vocal1.split(","))
                                sys.stdout.write(n)
                        elif g == "B":  #Donde haya una B, escoje una letra al azar, la muestra y la escribe al txt
                                n = random.choice(vocal2.split(","))
                                sys.stdout.write(n)
                        elif g == "C":  #Donde haya una C, escoje otra letra al azar, la muestra y la escribe al txt
                                n = random.choice(conso1.split(","))
                                sys.stdout.write(n)
                        elif g == "K":  #Donde haya una K, escoje otra letra al azar, la muestra y la escribe al txt
                                n = random.choice(conso2.split(","))
                                sys.stdout.write(n)
                        elif g == "S":  #Donde haya una S, escoje otra letra al azar, la muestra y la escribe al txt
                                n = random.choice(sufijos.split(","))
                                sys.stdout.write(n)
                        elif g == "P":  #Donde haya una P, escoje otra letra al azar, la muestra y la escribe al txt
                                n = random.choice(prefijos.split(","))
                                sys.stdout.write(n)
                        elif g == "T":  #Donde haya una T, escoje otra letra al azar, la muestra y la escribe al txt
                                n = random.choice(extra.split(","))
                                sys.stdout.write(n)
                        elif g != "\n":
                                sys.stdout.write(g)
                        yuno() #silaba[+1] así lee cada una de las letras de "silaba"
                print("")
                a += 1 # Contador +1, una palabra más.
                x = 0 #Reset silaba[0]
                silaba = random.choice(modelos.split(","))  #Elige un nuevo modelo de palabra

###----------- función que borra el texto en las entry
def limpia():
          e1.delete(0, END)
          e2.delete(0, END)
          e3.delete(0, END)
          sec.delete("1.0", END)
          resultados.delete("1.0", END)
###--------------- limpia          


###--------El cuadro de "Acerca de..."
def creditos():
        que = ("\n\nEscrito por Daniel Martínez.\nCSH Lingüística - UAM Iztapalapa\nFFyL,UNAM\n\nPara el taller de lenguas artificiales\nFacultad de Química, UNAM\nSeptiembre 2014\nCiudad de México\n\ndaniel.m.olivera@gmail.com\n\n")
        cre = Toplevel()
        cre.title("Acerca de conlanggen 2.1")
        l1 = Label(cre, text="\n\nconlanggen 2.1", font="bold", fg="white", bg="green")
        l1.grid(row=1, column=1)
        l2 = Label(cre, text=que)
        l2.grid(row=2, column=1)
        button = Button(cre, text="Ok", command=cre.destroy)
        button.grid(row=3, column=1)
###---------------- Acerca de...        


#---------- esta es la ventana de las instrucciones    
def ventana():
        top = Toplevel()
        top.title("Instrucciones")
        sc = Scrollbar(top)
        sc.pack(side=RIGHT, fill=Y)
        text = Text(top, width=60)
        text.config(yscrollcommand=sc.set)
        text.insert(END, instr)
        sc.config(command=text.yview)
        text.pack()
        button = Button(top, text="Ok", command=top.destroy)
        button.pack()
#------------ ventana de instrucciones

####---- Esta funcion se encarga de guardar al txt     
def guarda():
        paratxt = resultados.get('0.0', 'end')
        uno = e1.get()
        dos = e2.get()
        tres = e3.get()
        cuatro = e4.get()
        cinco = e5.get()
        seis = e6.get()
        siete = e7.get()
        m = sec.get('0.0', 'end')
        f = codecs.open('palabras.txt', mode='w', encoding='utf-8') #esto crea el archivo como file.open
        #file = open('palabras.txt', 'w')
        f.write("LISTA DE PALABRAS\n\n")
        #f.write("\n")
        #f.write("\n")
        f.write (time.strftime("%d/%m/%Y")) ## dd/mm/yyyy format
        #f.write("\n")
        f.write("\n------------------------\n")
        #f.write("\n")
        f.write("Configuraciones\n")
        #f.write("\n")
        f.write(uno)
        f.write("\n")
        f.write(dos)
        f.write("\n")
        f.write(tres)
        f.write("\n")
        f.write(cuatro)
        f.write("\n")
        f.write(cinco)
        f.write("\n")
        f.write(seis)
        f.write("\n")
        f.write(siete)
        f.write("\n")
        f.write(m)
        f.write("\n")
        f.write("------------------------")
        f.write("\n")
        f.write(paratxt)
        f.write("\n")
        f.write("\n")
        f.close()  #cierra el txt
        print('Lista guardada en "palabras.txt" ')
###---------------------- guardado en el txt




###################
###-------- Inicia el diseño de la ventana (del GUI)
###################
master = Tk()    #nombramos a la ventana principal como "master"
master.wm_title("conlanggen v. 2.1")  #el título de la ventana

#------- El menú de la ventana
menubar = Menu(master)

archivomenu = Menu(menubar)
archivomenu.add_command(label="Nuevo", command=limpia)
archivomenu.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Archivo", menu=archivomenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="Instrucciones", command=ventana)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de", command=creditos)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

master.config(menu=menubar) #mostrar el menú
#----------- Menú

###---- Aquí están las entry
nter = 7
Label(master, text="Vocales tipo 1 [V]:").grid(row=0, column=0, sticky=E)
Label(master, text="Vocales tipo 2 [B]:").grid(row=1, column=0, sticky=E)
Label(master, text="Consonantes tipo 1 [C]:").grid(row=2, column=0, sticky=E)
Label(master, text="Consonantes tipo 2 [K]:").grid(row=3, column=0, sticky=E)
Label(master, text="Sufijo [S]:").grid(row=4, column=0, sticky=E)
Label(master, text="Prefijo [P]:").grid(row=5, column=0, sticky=E)
Label(master, text="Suf - Pref (Extra) [T]:").grid(row=6, column=0, sticky=E)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

Label(master, text="-------------------------------------", foreground="gray").grid(row=nter, column=0, columnspan=2)

Label(master, text="Secuencias: ").grid(row=nter+1, column=0, sticky=E)
sec = Text(master, height=3, width= 23)
sec.grid(row=nter+1, column=1, sticky=W)


Label(master, text="-------------------------------------", foreground="gray").grid(row=nter+2, column=0, columnspan=2)

Label(master, text="Num. de palabras: ").grid(row=nter+3, column=0, sticky=E)
numm = Spinbox(master, from_=0, to=200, width=5)
numm.grid(row=nter+3, column=1, sticky=W)


Label(master, text="  ", foreground="gray").grid(row=nter+4, column=0, columnspan=2)

b = Button(master, text="Limpiar", width=10, command=limpia)
c = Button(master, text="GENERAR", width=10, command=motor)

b.grid(row=nter+5, column=0, sticky=E)
c.grid(row=nter+5, column=1)

Label(master, text="   ").grid(row=nter+6, column=0, columnspan=2)
Label(master, text="   ").grid(row=0, column=3)


###---------la textbox "principal"

scr = Scrollbar(master)
resultados = Text(master, height=15, width= 40, foreground="gray", yscrollcommand=scr.set)
resultados.insert(INSERT, """conlanggen 2.1

Agrega las vocales y consonantes
separadas por una coma.
Vocales [V]: a,e,i,o,u
Consoantes [C]: p,t,k,b,d,g

Agrega las secuencias que 
quieres combinar. Deben de ir en
mayúsculas y separadas por comas.
Secuencias: CVC,CVVC,CVCV,CTV,TVC

Indica cuántas palabras quieres generar

""")
scr.config(command=resultados.yview)
resultados.grid(row=0, rowspan=8, column=4)
scr.grid(rowspan=8,row=0,column=5, sticky=N+S)

####---------textbox

dd = Button(master, text="Guardar a .txt", width=10, command=guarda)
dd.grid(row=8, column=4)


sys.stdout = StdoutRedirector(resultados) # envía el ouput hacia el textbox

        


#Septiembre 14, 2014
#Generador de palabras conlanggen Ver. 2.1
#twitter: @jackeliand


mainloop()

#EOF
