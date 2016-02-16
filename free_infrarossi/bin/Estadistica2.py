#!/usr/bin/python
#-*- coding:utf-8 -*-
from numpy import *
import numpy as np
import matplotlib.pyplot as pl
import os
import subprocess
import math
import time
import shutil
import Gnuplot

class Estadistica:
    def Cargar(self):
	self.f= np.loadtxt('datos/dats1.dat')
	self.x = self.f[:,0]
	self.y= self.f[:,1]
	self.n = np.size(self.x)
	self.k = np.ceil(1 + np.log2(self.n)) # comando ceil redondea el numero al mayor entero
	self.c = np.sort(self.y) #comando sort guarda los datos de y
	self.lon = self.c[110]/8
	
	print "El tamaño de la muestra es: ", self.n , "\nEl tamaño del intervalo es ", self.k, self.lon

    def Clasificar(self):
	for i in range (0, 111):
	    a1 = self.y[i]
	    x = self.x[i]
	    b1 = float(a1)   
	    c1 = float(x)
#	    print a1, c1 
	    if  b1<=self.lon :
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter1-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter1-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

	    if  b1>=self.lon and b1< 2*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter2-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter2-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

	    if  b1 >= 2*self.lon and b1< 3*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter3-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter3-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

	    if  b1 >= 3*self.lon and b1< 4*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter4-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter4-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()


	    if  b1 >= 4*self.lon and b1< 5*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter5-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter5-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

	    if  b1 >= 5*self.lon and b1< 6*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter6-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter6-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

 	    if  b1 >= 6*self.lon and b1< 7*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter7-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter7-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()

	    if  b1 >= 7*self.lon and b1<= 8*self.lon:
		if c1<10:
		    print c1, "\t \t", b1
		    archi = open ('datos/inter8-0.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
	  	else: 
		    print c1, "\t \t", b1
 		    archi = open ('datos/inter8-1.dat','a+')
	            xo = str(c1)
	            yo = str (b1)
	            archi.write (xo)
	            archi.write ("\t ")
	            archi.write (yo)
	            archi.write("\n")
	            archi.close()
    def Marca(self):
	def Inter1():
	    x, y  = np.loadtxt('datos/inter1-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter1-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca1.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca2.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter1-0.dat datos/inter1-1.dat")	    

	
	def Inter2():
	    x, y  = np.loadtxt('datos/inter2-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter2-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca3.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca4.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter2-0.dat datos/inter2-1.dat")	    

	def Inter3():
	    x, y  = np.loadtxt('datos/inter3-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter3-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca5.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca6.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter3-0.dat datos/inter3-1.dat")	    

	def Inter4():
	    x, y  = np.loadtxt('datos/inter4-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter4-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca7.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca8.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter4-0.dat datos/inter4-1.dat")	    

	def Inter5():
	    x, y  = np.loadtxt('datos/inter5-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter5-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca9.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca10.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter5-0.dat datos/inter5-1.dat")

	def Inter6():
	    x, y  = np.loadtxt('datos/inter6-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter6-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca11.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca12.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter6-0.dat datos/inter6-1.dat")


	def Inter7():
	    x, y  = np.loadtxt('datos/inter7-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter7-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca13.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca14.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter7-0.dat datos/inter7-1.dat")

	def Inter8():
	    x, y  = np.loadtxt('datos/inter8-0.dat', unpack=True,  usecols=[0,1])
	    x1, y1 = np.loadtxt('datos/inter8-1.dat', unpack=True,  usecols=[0,1])
	    xp = x.size
	    yp = y.size
	    xp1 = x1.size
	    yp1 = y1.size
	    X = round(float(np.sum(x)/xp), 4)
	    Y = round(float(np.sum(y)/yp), 4)
	    X1 = round(float(np.sum(x1)/xp1), 4)
	    Y1 = round(float(np.sum(y1)/yp1), 4)
	    np.savetxt('datos/marca15.dat', column_stack((X,Y)), fmt=('%6.3f', '%6.3f'))
	    np.savetxt('datos/marca16.dat', column_stack((X1,Y1)), fmt=('%6.3f', '%6.3f'))
	    os.system("rm datos/inter8-0.dat datos/inter8-1.dat")
	

	def Estad():
	    x1, y1 = np.loadtxt("datos/marca1.dat", unpack=True,  usecols=[0,1])
	    x2, y2 = np.loadtxt("datos/marca2.dat", unpack=True,  usecols=[0,1])
	    x3, y3 = np.loadtxt("datos/marca3.dat", unpack=True,  usecols=[0,1])
	    x4, y4 = np.loadtxt("datos/marca4.dat", unpack=True,  usecols=[0,1])
	    x5, y5 = np.loadtxt("datos/marca5.dat", unpack=True,  usecols=[0,1])
	    x6, y6 = np.loadtxt("datos/marca6.dat", unpack=True,  usecols=[0,1])
	    x7, y7 = np.loadtxt("datos/marca7.dat", unpack=True,  usecols=[0,1])
	    x8, y8 = np.loadtxt("datos/marca8.dat", unpack=True,  usecols=[0,1])
	    x9, y9 = np.loadtxt("datos/marca9.dat", unpack=True,  usecols=[0,1])
	    x10, y10 = np.loadtxt("datos/marca10.dat", unpack=True,  usecols=[0,1])
	    x11, y11 = np.loadtxt("datos/marca11.dat", unpack=True,  usecols=[0,1])
	    x12, y12 = np.loadtxt("datos/marca12.dat", unpack=True,  usecols=[0,1])
	    x13, y13 = np.loadtxt("datos/marca13.dat", unpack=True,  usecols=[0,1])
	    x14, y14 = np.loadtxt("datos/marca14.dat", unpack=True,  usecols=[0,1])
	    x15, y15 = np.loadtxt("datos/marca15.dat", unpack=True,  usecols=[0,1])
	    x16, y16 = np.loadtxt("datos/marca16.dat", unpack=True,  usecols=[0,1])
	    self.Xm1= float(x14 - x13)
	    self.xr1 = x13
	    self.xr2 = x14
	    X = [x1, x3, x5, x7, x9, x11, x13, x15, x16, x14, x12, x10, x8, x6, x4, x2]
	    Y = [y1, y3, y5, y7, y9, y11, y13, y15, y16, y14, y12, y10, y8, y6, y4, y2]
	    np.savetxt('datos/marca_clase.dat', column_stack((X, Y)), fmt=('%6.3f', '%6.3f'))
	    print "Esta es la distancia para el primer orden de difraccion ", self.Xm1, "centimetros"
	    
	def Difraccion():
#--------------------------- Numero de lineas por milimetro de la rejilla 103 -----------------
#--------------------------- Distancia entre linea y linea de la rejilla 4.81^(-6) metros		    
# ------------------------- Distancia de separacion de la rejilla con la pantalla 40^(-2) metros
	    d = 4.81*10**(-6)
	    x = self.Xm1*10**(-2)
	    y = 45*10**(-2)
	    tetharad = math.atan(x/y)
	    tethagra = math.degrees(tetharad)
#	    lamda = tetharad*d
	    sintetha= math.sin(tetharad)
	    self.lamda = round((2*d*sintetha)*10**(9),2)
	    self.error = round(pow(pow(800-self.lamda,2),0.5), 2)
	    print tethagra, "\n ", sintetha
	    print "la longitud de onda aproximada para el diodo infrarrojo es",  self.lamda	, "nanometros, con un error de ", self.error , " %" 
	
        
	def Grafica():
#	    pl.ion()
	    x1, y1 = np.loadtxt("datos/dats1.dat", unpack=True,  usecols=[0,1])
	    self.x = x1/100
	    self.y = y1 /1000
	    pl.subplot(221)
	    #time.sleep(10)
	    pl.plot(self.x,self.y, 'o--')
	    pl.title('Datos Capturados  \n')
	    pl.xlabel('Distancia [m]')
	    pl.ylabel('Voltaje [V]')


    	def Graf2():
	    x10, y10 = np.loadtxt("datos/marca_clase.dat", unpack=True,  usecols=[0,1])
	    self.x11 = x10/100
	    self.y11 = y10/1000
	    pl.subplot(222)
            pl.plot(self.x11, self.y11, 'o--')
            pl.title('Patrones de Interferencia \n')
 	    pl.xlabel('Distancia [m]')
	    pl.ylabel('Voltaje [V]')
	    pl.text(0.06, 0.010, r' x1 = ' + str(self.xr1/100))
	    pl.text(0.06, 0.006, r' x2 = ' + str(self.xr2/100))
	    pl.text(0.045	, 0.002, r' x2-x1 = ' + str(self.Xm1/100))
 	    pl.ylim(0, 0.036) 
        
	def Graf3():
	    self.x13, self.y13 = np.loadtxt("datos/marca13.dat", unpack=True,  usecols=[0,1])
	    self.x14, self.y14 = np.loadtxt("datos/marca14.dat", unpack=True,  usecols=[0,1])
            pl.subplot(212)
            pl.plot(self.x, self.y, 'G')
            pl.plot(self.x11, self.y11, 'o--')
#	    pl.annotate(u'Máximo', xy = (self.x13, self.y13), xycoords = 'data' ,xytext = (self.x13 - 0.005, self.y13 + 0.004),  arrowprops = dict(arrowstyle = "->"))
#	    pl.arrow(self.x13, self.y13, 0.10, 0.010)
	    pl.text(0.06, 0.010, r' Longitud con m=1 :  ' + str(self.Xm1/100) + '[m] ')
	    pl.text(0.04, 0.005, r' Lamda IRE = ' +  str(self.lamda) + ' [nm}      +/- ' + str(self.error) + ' [nm]')
 	    pl.ylim(0, 0.036) 
	    pl.xlabel('Distancia [m]')
	    pl.ylabel('Voltaje [V]')
            pl.title('LONGITUD DE ONDA DIODO INFRARROJO \n')
            pl.legend(loc='upper left')
             

   	def Plotear():
            pl.subplots_adjust(right=0.97)
            pl.subplots_adjust(left=0.11)
            pl.subplots_adjust(bottom=0.13)
            pl.subplots_adjust(top=0.87)
            pl.subplots_adjust(wspace=0.32)
            pl.subplots_adjust(hspace=0.71)
            pl.savefig('datos/Graficas.png')
	    Grafica()
            pl.show()

	def Pausa():
	    time.sleep(2)
	    self.Ordenar()    

	def init():
	    Inter1()
	    Inter2()
	    Inter3()
	    Inter4()
	    Inter5()
	    Inter6()
	    Inter7()
	    Inter8()
	    Estad()
	    Difraccion()
	    Grafica()
	    Graf2()
	    Graf3()
	    Plotear()
	    Pausa()
	init()
    def Ordenar(self):
	os.system("python bin/o_Carpetas1.py")

    def __init__(self):
	self.Cargar()
	self.Clasificar()
	self.Marca()
esto = Estadistica()
