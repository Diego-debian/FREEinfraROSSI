#/usr/bin/python
#!*-* coding:utf-8 *-* 
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad  Distrital Francisco Jose  
# Grupo de fisica e informatica
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.
import numpy as np
import os
import serial
import subprocess
import math
import time
import Gnuplot
import shutil
import matplotlib.pylab as pl
class App:  
    def Analisis(self):
#	os.system("octave datos/estadistica1.m")
	os.system("octave estadistica1.m")
	f = np.loadtxt("datos/F.dat")	
	a = np.loadtxt("datos/a.dat")
	b = np.loadtxt("datos/b.dat")
	self.Yest = np.loadtxt("datos/Yest.dat")	
	self.Yteo = np.loadtxt("datos/Yteo.dat")	
	self.ECM = np.loadtxt("datos/ECM.dat")
	self.ECM1 = round(self.ECM, 11)
	self.X = f[:,0]
	self.V = f[:,1]
	self.a = round(a, 6)
	self.b = round(b, 3)
	self.error = ((-2-float(self.b))**2)**0.5
	print self.X, self.V,"\n\n\n", self.a," X^(",self.b,")  " 

    def Grafica(self):
	pl.subplot(221)
        pl.title('Distancia vs Intensida \n')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Intensidad [W]')
	pl.plot(self.X, self.V, 'o --')
	pl.axis([0, 0.65, -0.001, 0.022])
        pl.text(0.2, 0.019, r'Datos recolectados')



    def Grafica1(self):
        pl.subplots_adjust(left=0.13)
        pl.subplots_adjust(bottom=0.13)
        pl.subplots_adjust(right=0.97)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.37)
        pl.subplots_adjust(hspace=0.68)
	

    def Grafica2(self):
	pl.subplot(222)
        pl.title('APROXIMACION')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Intensidad [W]')
        pl.plot(self.X, self.V, 'B')
        pl.plot(self.X, self.Yest, 'R')
	pl.axis([0, 0.65, -0.001, 0.020])
        pl.text(0.3, 0.017, r'Azul')
        pl.text(0.15, 0.015, r'' +"("+ str(self.a) + ")"+ '*X^('+ str(self.b)+')')
        pl.text(0.2, 0.010, r'Rojo')
        pl.text(0.19, 0.008, r'' +"(" + str(self.a) + ")"+ '*X^(-2)')

        
    def Grafica3(self):
        pl.subplot(212)
	pl.plot(self.X, self.V, 'K')
        pl.plot(self.X, self.Yteo, 'R')
        pl.plot(self.X, self.Yest, 'B')
        pl.subplot(212)
        pl.xlabel('Distancia [m]')
        pl.ylabel('Intensidad [W]')
        pl.title('Distancia vs Intensidad irradiada \n')
        pl.legend(loc='upper left')
	pl.axis([0, 0.65, -0.001, 0.022])
	pl.text(0.3, 0.02, r'Azul I_r=' + str(self.a) + '*X^('+ str(self.b)+')')
        pl.text(0.3, 0.017, r'Rojo I_r=' + str(self.a) + '*X^(-2)')
        pl.text(0.3,0.014, r'ECM = ' + str(self.ECM1))
        pl.text(0.3,0.011, r'E_exp = ' + str(self.error))
        pl.savefig('datos/Atenuacion.png')
        pl.show()

    def Ordenar(self):
	os.system("python bin/o_Carpetas.py")

    def __init__(self):
	self.Analisis()
	self.Grafica()
	self.Grafica1()
	self.Grafica2()
	self.Grafica3()
#	self.Ordenar()
        self.__del__()
            
    def __del__(self):
        print ("PROGRAMA TERMINADO")
                
                
Iniciar  = App()
