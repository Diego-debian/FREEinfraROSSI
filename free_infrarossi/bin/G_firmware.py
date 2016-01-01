#!/usr/bin/python
# *-* coding:utf-8 *-*

# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad Distrital Francisco Jose  
# Grupo de fisica e informatica
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.

import numpy as np
import pylab as pl
import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox
import Tkinter
import shutil

class G_firmware:
    def Pendulo(self):
	def Salir():
	    tkMessageBox.showinfo("free_pops_1.0", message= "! Cerrando el programa ¡")
            exit() 
	
	def Continuar():
	    tkMessageBox.showinfo("free_pops_1.0", message= "Cargando el firmware en la tarjeta microcontroladora. \n\n si no carga el firmware: \n\n* Revise su conexión con la tarjeta programadora arduino uno. \n\n* Revise el microcontrolador que este funcionando bien ")
	    os.system("python bin/firmware/firmware_free_pops.py &")

	bicho = Tk()
        bicho.geometry("280x400+507+60")
        bicho.config(bg="white")
        bicho.title("free_pops_1.0")
        bicho.resizable(width=0, height=0)
	yn= -200
	xn = -350
	imgBoton2=PhotoImage(file="Imagenes/cap8.gif")
        btnLogo= Label(bicho, image=imgBoton2,  height=150, width =180).place(x=400+xn, y=215+yn)
        lblFisinfor = Label(bicho, text=" GRUPO DE FISICA E INFORMATICA ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=360+xn, y=371+yn)
	lblInfo = Label(bicho, text="Dr. Julian Andres Salamanca\n Diego Alberto Parra Garzón", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=400+xn, y=390+yn)
        lblFisinfor = Label(bicho, text="DEBE TENER LA TARJETA \nMICROCONTROLADORA ARDUINO\n CONECTADA PARA CONTINUAR", fg = ("red"), bg = ("white"), font = ("Century Schoolbook L",11)).place(x=350+xn, y=460+yn)
	btnSalir=Button(bicho, text = "Salir", command=Salir, height=1, width =5).place(x=20, y=360)
	btnContinuar=Button(bicho, text = "Continuar", command=Continuar, height=1, width =5).place(x=160, y=360)

	bicho.mainloop()  

 

    def __init__(self):
        self.Pendulo()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")

if __name__ == "__main__":
    G_firmware()
