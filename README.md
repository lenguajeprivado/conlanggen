# conlanggen Ver 2.1


### Generador de palabras


*Word generator for conlangs (in spanish)*

Este es un generador de palabras para crear diccionarios conlangs (lenguas artificiales).
Su funcionamiento es muy simple.

1. Agregas algunas vocales y consonantes
2. Indicas la estructura fonotáctica CVCVCV...
3. Le dices cuántas palabras quieres en tu lista.

Dentro del programa vienen instrucciones completas de uso.

## Instalación

Existen tres maneras de instalar en Linux.

#### Haciendo una copia de todo este repositorio de GitHub

Para instalarlo desde el repositorio (en Ubuntu, Linux Mint, Debian, etc) en la terminal escribe:

    # instalar git
    sudo apt-get install git

    # crea un directorio "conlanggen" y entra
    mkdir -p ~/conlanggen && cd ~/conlanggen

    # copiar desde el repositorio
    git clone https://github.com/jackeliand/conlanggen.git

#### Bajando un sólo archivo comprimido

[Baja este archivo a tu computadora](https://github.com/jackeliand/conlanggen/raw/master/conlanggen) y puedes utilizarlo como un ejecutable más, dandole doble click o escribiendo:

    ./conlanggen
    
#### Bajando el código directamente.

[Baja el programa principal](https://github.com/jackeliand/conlanggen/raw/master/conlanggen.py) y el [archivo de ayuda](https://github.com/jackeliand/conlanggen/raw/master/info.py). 

Colocalos en una misma carpeta y úsalos como cualquier otro archivo de Python. 

En la terminal escribe

    python conlanggen.py
    
## Versión para Windows

Elaboré una versión para usar en Windows.

Es completamente funcional. [Encuentrala aquí](https://github.com/jackeliand/conlanggen/tree/master/Win)

## Screenshots

![Lengua negra](/screenshots/01.jpg)

![conlanggen 2.1](/screenshots/02.jpg)


## Notas de la versión.

1.0 Versión solo en CLI

1.5 Reparados errores menores

2.0 Versión en GUI

2.1 Reparado el scroll

## Acerca de...
Hice este programa para aprender a usar Python. 
Está escrito en la versión 2.7.6

Llevo poco de aprender este lenguaje. No soy programador; soy lingüísta, y persona de letras... así que seguramente tendré muchos vicios y errores en la forma en la que está estructudado el código.

Creé este programa para usarlo en el "Taller de lenguas artificiales" que imparto en la FQ, UNAM (México).

Es gratis.
Si te parece un programa útil y quieres mejorarlo, sientete libre de hacer un fork de él (recuerda mencionarme en algun lugar del nuevo código).

&copy; Daniel Martínez <daniel.m.olivera@gmail.com>

Twitter: [@jackeliand](http://twitter.com/JackEliand)

## Copyleft

[GNU GPL v2.0](http://www.gnu.org/licenses/gpl-2.0.txt)
