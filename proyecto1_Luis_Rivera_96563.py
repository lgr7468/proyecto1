# Nombre: Luis G. Rivera-Garcia
# Numero de estudiante: 93563
# Email: rivera_96563@students.pupr.edu

#Project 01: Simple Python Game
#Description
#Write a simple game of your own imagination or use one from the Internet as a reference or starting point.

#Objective
#The main objective of this project is to practice the basic elements of Python programming seen so far.

#Requirements
#Your code should use only the graphics.py library and basic elements of the language seen so far such as 
# lists, strings, files, functions and control structures. You can integrate getKey/getMouse or checkKey/checkMouse 
# events. Also, update to control the speed how elements are drawn in your window. You must create a README 
# file at GitHub describing your game.

#To submit your homework, just enter your GitHub repository URL. An intro to Git will be given by our TA, Samuel Matos.

#Notes:
#See some game ideas at http://www.grantjenks.com/docs/freegames/
#HW04 has simple code that you can use as a starting point
#If you choose an Internet game and use a code base version, you must justify the reason for your choice and clearly 
# show the new features that you included that satisfy the previous requirements.
#Reference the base code link

from graphics import *

# Funcion que creara un cuadro que tapara la pregunta y respuesta anterior.
def taparAnterior():
    tapar = Rectangle(Point(0, 240), Point(999, 999))
    tapar.setFill("#faf3dd")
    tapar.setOutline("#faf3dd")
    tapar.draw(win)

# Funcion que creara dos lineas de texto con instrucciones iniciales para el usuario
def instruccionesIniciales():
    instr = Text(Point(320, 100), "Bienvenido a la trivia! Tendras que contestar 5 preguntas para cualificar.")
    instr.setSize(14)
    instr.setTextColor("black")
    instr.draw(win)

    instr2 = Text(Point(220, 130), "Cuando estes listo(a), haz click para comenzar.")
    instr2.setSize(14)
    instr2.setTextColor("black")
    instr2.draw(win)

def validarSeleccion(seleccion, respuesta):
    if (seleccion == respuesta):
        resultado = Text(Point(500, 400) , "CORRECTO!")
        resultado.setSize(28)
        resultado.setTextColor("#00509d")
        resultado.draw(win)
    else:
        resultado = Text(Point(500, 400) , "INCORRECTO!")
        resultado.setSize(28)
        resultado.setTextColor("#c5202d")
        resultado.draw(win)

#Create a window
win = GraphWin("Trivia", 1000, 600)
win.setBackground("#faf3dd")

# Top Banner
banner = Text(Point(500, 30), "Trivia")
banner.setSize(26)
banner.setTextColor("#DB2763")
banner.setStyle("bold")
banner.draw(win)

# Instrucciones para el usuario
instruccionesIniciales()

win.getMouse()

# Lista de preguntas:
preguntas = ["Cual es la capital de Turquia?",\
            "Cual era la ciudad hogar de Marco Polo?",\
            "Quien invento el telescopio reflector?",\
            "Que seleccion de futbol gano el Mundial Brasil 2014?",\
            "El proceso por el que una celula se divide para formar dos celulas hijas se llama:"]

# Lista de opciones
opciones = [["Ankara", "Tegucigalpa", "Estambul", "Ninguna"],\
            ["Roma", "Berlin", "Venecia", "Singapur"],\
            ["Isaac Newton", "Albert Einstein", "Nicolas Copernico", "Ninguno"],\
            ["Espana", "Alemania", "Polonia", "Brasil"],\
            ["Mitosis", "Meiosis", "Segregacion", "Ninguna"]]

# Lista de respuestas
respuetas = [1, 3, 1, 2, 1]

# Iterar sobre las preguntas y opciones
for pregunta, opcion_list, respuesta in zip(preguntas, opciones, respuetas):
    # Dibujar pregunta
    preg_text = Text(Point(500, 250), pregunta)
    preg_text.setTextColor("black")
    preg_text.setSize(20)
    preg_text.draw(win)

    # Dibujar opciones y sus bordes
    borde = Rectangle(Point(50,300), Point(250, 350))
    borde.draw(win)
    opcion_text = Text(borde.getCenter(), "(1) " + opcion_list[0])
    opcion_text.draw(win)

    for opcion,i in zip(opcion_list, range(0,len(opcion_list))):
        borde1 = borde.clone()
        borde1.move(220*i, 0)
        borde1.draw(win)
        opcion_text = Text(borde1.getCenter(), "(" + str(i + 1) + ") " + opcion)
        opcion_text.draw(win)

    # Capturar seleccion del usuario en el teclado (convertirla de str a int para poder hacer validaciones)
    seleccion = int(win.getKey())

    # Validar seleccion contra la respuesta correcta
    validarSeleccion(seleccion, respuesta)
    
    # Aguardar al usuario hacer click para pasar a la siguiente pregunta
    win.getMouse()
    
    # Tapar preguntas anteriores con un cuadro del mismo color del fondo (undraw no funciona pues use un loop)
    taparAnterior()


win.getMouse()
win.close()