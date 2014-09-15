#conlanggen Ver 1.0 

##Generador de palabras

*Word generator for conlangs (in spanish)*

Este es un generador de listas de palabras para crear diccionarios de lenguas artificiales (conlangs).
Su funcionamiento es muy simple.

1. Agregas algunas vocales y consonantes
2. Indicas la estructura fonotáctica CVCVCV...
3. Le dices cuántas palabras quieres en tu lista.

Dentro del programa vienen instrucciones completas de uso.

##Instalación
Para instalarlo desde el repositorio, en la terminal escribe:

    # instalar git
    sudo apt-get install git

    # crea un directorio "conlanggen" y entra
    mkdir -p ~/conlanggen && cd ~/conlanggen

    # copiar desde el repositorio
    git clone https://github.com/jackeliand/conlanggen.git

(¿Únicamente usas Windows? Tendías que tener [esto](https://windows.github.com/) para bajar los repositorios de Git Para saber cómo se usa lee [estas instrucciones](https://windows.github.com/help.html) ).

##Uso
Para usarlo, escribe en la terminal

    python conlanggen.py

(Si usas Windows necesitas tener instalado [Python para Windows](https://www.python.org/download). Si necesitas instrucciones de cómo se usa, [revisa estas instrucciones](http://learnpythonthehardway.org/book/ex0.html). )

##Acerca de...
Hice este programa para aprender a usar Python. 
Está escrito en la versión 2.7.6
Llevo poco de aprender este lenguaje. No soy programador; soy lingüísta, así que seguramente tendré muchos vicios en la forma en la que está estructudado el código.
Creé este programa para usarlo en el "Taller de lenguas artificiales" que imparto en la FQ, UNAM (México).
Es gratis.
Si te parece un programa útil y quieres mejorarlo, sientete libre de hacer un fork de él (recuerda mencionarme en algun lugar del nuevo código).

&copy; Daniel Martínez <daniel.m.olivera@gmail.com>

Twitter: [@jackeliand](http://twitter.com/JackEliand)

## Copyleft

[GNU GPL v2.0](http://www.gnu.org/licenses/gpl-2.0.txt)
