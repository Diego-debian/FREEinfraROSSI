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
    def Verifica(self):
	os.system('rfcomm  -a  > conexion.txt | cut -d ":" -f 1,1  conexion.txt > direccion.txt ')
	puerto = open('direccion.txt', 'r')
	self.puerto = puerto.read(7)
	puerto.close()
	self.puerta = "/dev/"+self.puerto
	print self.puerta
        try:       
            arduino = serial.Serial(self.puerta, 9600)
            arduino.write("aa")
  	except:
	    os.system("exit")

    def Salir(self):
        exit()
                
    def Comenzar(self):
        # MAXIMO n en el for 130
        # Distancia de separacion 27 cm
	# Distancia de recoleccion 25 cm
	#Paso en centimetros pausada 1 = 0,34
        #Paso en centimetros pausada 2 = 0,30
        #Paso en centimetros pausada 3 = 0,27
        #Paso en centimetros pausada 4 = 0,213
        #Paso en centimetros pausada 5 = 0.205
        for n in range (0, 117): 
            os.system('rm datos/dat.dat')
            #time.sleep(2)
            arduino= serial.Serial(self.puerta, 9600)
	    print "aca va la lectura"
            arduino.write("aa")
            #time.sleep(1)
            arduino.write('5')
            arduino.close()
            arduino=serial.Serial(self.puerta, 9600)
            time.sleep(2)
            arduino.write('zz')
            for i in range(0, 140):
                arduino=serial.Serial(self.puerta, 9600)
                archi = open('datos/dat.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = 0.205*2*(132 - n)
                xo = str(z)
                yo = str(x)
                print "paso numero", n
                print "(cm) \t (mV)"
                print('{0} {1}').format(xo, yo)
                archi.write (xo)
                archi.write (" ")
                archi.write (yo)
                archi.close()  
            else:
		os.system("octave bin/prom1.m")
		archi = open('datos/prom.dat', 'a+')
                print("aca va la pausa")
                Lectura = archi.read()
                archi.close() 
                archi1 = open('datos/dats1.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                arduino.write('aa')
                arduino.close()

    def Analisis(self):
	os.system("octave bin/estadistica1.m")
#	os.system("octave estadistica1.m")
	self.BX = np.loadtxt("datos/BX.dat")
	self.BY = np.loadtxt("datos/BY.dat")
	self.error_CM1 = np.loadtxt("datos/ECM1.dat")
	self.q1 = np.loadtxt("datos/q1.dat")
	self.Amplitud = np.loadtxt("datos/Amplitud.dat")
	self.Ampli = round(self.Amplitud, 4)	
	self.T = np.loadtxt("datos/Transmitancia.dat")	
	self.A = np.loadtxt("datos/Vteo.dat")	
	self.V_A = np.loadtxt("datos/V_aproximado.dat")
	f = np.loadtxt("datos/F.dat")	
	a = np.loadtxt("datos/a.dat")
	b = np.loadtxt("datos/b.dat")
	self.Yest = np.loadtxt("datos/Yest.dat")	
	self.Yteo = np.loadtxt("datos/Yteo.dat")	
	self.ECM = np.loadtxt("datos/ECM.dat")
	self.error_CM11 = round(self.error_CM1, 5)
	self.X = f[:,0]
	self.V = f[:,1]
	self.a = round(a, 4)
	self.b = round(b, 3)
	print self.X, self.V,"\n\n\n", self.a," X^(",self.b,")  " 

    def Grafica(self):
	pl.subplot(221)
        pl.title('Distancia vs Voltaje \n')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
	pl.plot(self.X, self.V, 'g:o')
	pl.axis([0, 0.6, 0, 2])
        pl.text(0.2, 4, r'Datos recolectados')
	pl.text(0.3, 0.6, r'Datos' )



    def Grafica1(self):
        pl.subplots_adjust(right=0.97)
        pl.subplots_adjust(left=0.1)
        pl.subplots_adjust(bottom=0.13)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.24)
        pl.subplots_adjust(hspace=0.60)
	

    def Grafica2(self):
	pl.subplot(222)
        pl.title('APROXIMACION')
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
        pl.plot(self.X, self.A, 'B', self.q1, self.BY, 'y', self.q1, self.BX, 'b')
        pl.plot(self.X, self.V_A, 'Y', self.X, self.V, 'g:o')
	pl.axis([0, 0.6, 0, 4])
	pl.text(0.2, 3, r'V1  = ' + str(0.0277) + '  X^('+ str(-2)+')')
	pl.text(0.12, 3.5, r'V1' )
	pl.text(0.01, 1, r'V2*' )
        pl.text(0.2, 2.5, r'V2*  = ' + str(self.Ampli) + '  X^(-2)')

        
    def Grafica3(self):
        pl.subplot(212)
	pl.plot(self.X, self.V, 'g:o', self.X, self.V_A, 'Y', self.X, self.A, 'B', self.q1, self.BY, 'y', self.q1, self.BX, 'b')
        pl.subplot(212)
        pl.xlabel('Distancia [m]')
        pl.ylabel('Voltaje [V]')
        pl.title('Distancia vs Voltaje \n')
        pl.legend(loc='upper left')
	pl.axis([0, 0.6, 0, 4])
	pl.text(0.35, 3, r'V1=  ' + str(0.0277) + '  X^('+ str(-2)+')')
        pl.text(0.35, 2.5, r'V2*=  ' + str(self.Ampli) + '  X^(-2)')
	pl.text(0.12, 3.5, r'V1' )
	pl.text(0.01, 2, r'V2*' )
        pl.text(0.35, 2, r'Fp = ' + str(round(self.T,4)))
        pl.text(0.35, 1.5, r'ECM = ' + str(round(self.error_CM1,7)))
        pl.savefig('datos/Absorcion.png')
        pl.show()
	
    def Ordenar(self):
	os.system("python bin/o_Carpetas.py")


                
    def __init__(self):
	self.Verifica()
        self.Comenzar()
	self.Analisis()
	self.Grafica()
	self.Grafica1()
	self.Grafica2()
	self.Grafica3()
	self.Ordenar()
        self.__del__()
            
    def __del__(self):
        print ("PROGRAMA TERMINADO")
                
                
Iniciar  = App()
