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
#	self.f= np.loadtxt('datos/dats1.dat')
	self.f= np.loadtxt('dats1.dat')
	self.x = self.f[:,0]
	self.y= self.f[:,1]
	self.n = np.size(self.x)
	self.k = np.ceil(1 + np.log2(self.n)) # comando ceil redondea el numero al mayor entero
	self.c = np.sort(self.y) #comando sort guarda los datos de y
	self.lon = self.c[110]/8
	
	print "El tamaño de la muestra es: ", self.n , "\nEl tamaño del intervalo es ", self.k, self.lon
 
    def Cargar1(self):
#	self.f= np.loadtxt('datos/datos_2.dat')
	self.f= np.loadtxt('datos_2.dat')
	self.o = self.f[:,0]
	self.p= self.f[:,1]
	self.q = np.size(self.o)
	self.r = np.ceil(1 + np.log2(self.q)) # comando ceil redondea el numero al mayor entero
	self.s = np.sort(self.p) #comando sort guarda los datos de y
	self.slon = self.c[110]/8
	
	print "El tamaño de la muestra es: ", self.q , "\nEl tamaño del intervalo es ", self.r, self.slon

    def Clasificar(self):
#	os.system("rm datos/datos_2.dat")
	os.system("rm datos_2.dat")
	for i in range (0, self.n):
	    a1 = self.y[i]
	    a2 = self.y[i-1]
	    a3 = self.y[i-2]
	    a4 = self.y[i-3]
	    x = self.x[i]
	    x1 = self.x[i-1]
	    x2 = self.x[i-2]
	    x3 = self.x[i-3]
	    b1 = float(a1)   
	    c1 = float(x)
#	    print a1, c1 
            
	    if a1 < a2  and a2 > a3  :
		print "\n", a1, "\t", x1
		print "\n", a2, "\t", x2
		print "\n", a3, "\t", x3
#		archi = open ('datos/datos_2.dat','a+')
		archi = open ('datos_2.dat','a+')
		xo1 = str(x1)	
	        yo1 = str (a1)
		xo2 = str(x2)	
	        yo2 = str (a2)
		xo3 = str(x3)	
	        yo3 = str (a3)
#	        archi.write (xo3)
#        	archi.write ("\t ")
#        	archi.write (yo3)
#        	archi.write("\n")
		archi.write (xo2)
        	archi.write ("\t ")
        	archi.write (yo2)
        	archi.write("\n")
# 		archi.write (xo1)
#        	archi.write ("\t ")
#        	archi.write (yo1)
#        	archi.write("\n")
        	archi.close()

    def Clasificar1(self):
#	os.system("rm datos/datos_3.dat")
	os.system("rm datos_3.dat")
	for i in range (0, self.q):
            self.Cargar1()
	    a1 = self.p[i]
	    a2 = self.p[i-1]
	    a3 = self.p[i-2]
	    a4 = self.p[i-3]
	    x = self.o[i]
	    x1 = self.o[i-1]
	    x2 = self.o[i-2]
	    x3 = self.o[i-3]
	    b1 = float(a1)   

#	    print a1, c1 
            
	    if a1 <= a2  and a2 > a3  :
		print "\n", a1, "\t", x1
		print "\n", a2, "\t", x2
		print "\n", a3, "\t", x3
#		archi = open ('datos/datos_3.dat','a+')
		archi = open ('datos_3.dat','a+')
		xo1 = str(x1)	
	        yo1 = str (a1)
		xo2 = str(x2)	
	        yo2 = str (a2)
		xo3 = str(x3)	
	        yo3 = str (a3)
#	        archi.write (xo3)
#        	archi.write ("\t ")
#        	archi.write (yo3)
#        	archi.write("\n")
		archi.write (xo2)
        	archi.write ("\t ")
        	archi.write (yo2)
        	archi.write("\n")
# 		archi.write (xo1)
#        	archi.write ("\t ")
#        	archi.write (yo1)
#        	archi.write("\n")
        	archi.close()




    def __init__(self):
	self.Cargar()
	self.Clasificar()
	self.Cargar1()
	self.Clasificar1()
	#self.Marca()
esto = Estadistica()
