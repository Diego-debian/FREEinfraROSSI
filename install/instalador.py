#/usr/bin/python
#!*-* coding:utf-8 *-* 

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

import os 
import time
class Instalador:
    def Presentacion(self):
	os.system("clear")
	print chr(27)+"[2;32m"+"\n\n\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	print "\t\t  Instalador de free_infrarrosi"  
	print "\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  
	print chr(27)+"[0m"+"\n \n \n \t Bienvenido al software free_infrarrosi, el cual le permitira tener\n\t varias horas de diversión; este software fue diseñado para el control,\n\t recolección y análisis de datos del vehículo motorizado infrarrosi,\n\t el cual permite ilustrar el estudio de las propiedades de las ondas\n \t electromagnéticas en el espectro infrarrojo, tales como la difracción,\n\t atenuación y absorción. DiSfrutara de una interfaz amigable al usuario. "
	print "\n\n\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	print chr(27)+"[5;36m"+"\t\t DESEA CONTINUAR CON LA INSTALACION: "
	print chr(27)+"[0m"+"\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	print "\t Oprima 1 para si \n\t Oprima 2 para no"
	Pr1 = int(raw_input("Ingrese su respuesta: "))
	if Pr1 == 1:
	    self.Instalar()
	elif Pr1 ==2:
	    self.exit()
	    os.system("killall python")
	else: 
	    self.exit()
	    os.system("killall python")
    def Instalar(self):
	os.system("clear")
	print chr(27)+"[2;32m"+"\n\n ¿Que desea hacer ?\n\n"
	print chr(27)+"[0m"+"\n \t oprima 1 para instalar free_infrarrosi"
	print "\n \t Oprima 2 para desinstalar free_infrarrosi"
	print chr(27)+"[3;36m"+"\n \t Oprima cualquier tecla para SALIR del instalador\n \n"
	Pr2 = int(raw_input(chr(27)+"[5;32m"+"Ingrese su petición : "+chr(27)+"[0m"))
	if Pr2 == 1:

	    os.system("apt-get update ")
	    os.system("apt-get install xterm bluez* gcc g++ emacs gnuplot gnuplot-qt evince octave python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm* arduino fritzing binutils")
	    archi = open('/etc/bash.bashrc', 'a+')
	    archi.write("\ninfrarossi='cd ~/Documentos/Free-infrarrosi/free_infrarossi && ./infrarrosi'")
	    archi.close()
	    print chr(27)+"[5;33m"+"INSTALACION TERMINADA "
	    print "reinicie su pc"

	elif Pr2 == 2:
#	    os.system("apt-get --purge remove emacs gnuplot gnuplot-qt evince octave python-matplotlib  python-scipy python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm* arduino fritzing")
#	    os.system("apt-get autoremove")
#	    os.system("apt-get update")
	    os.system("bash unistall.sh")
	    print " DESINSTALACION EXITOSA "
	    print  "Se ha creado una copia de respaldo del archivo /etc/bash.bashrc como /etc/bash.bashrc.respaldo, si tiene algun problema con este archivo despues de la desinstalación, solamente ejecute este comando en la terminal con permisos de administrador y sin las comillas 'cp /etc/bash.bashrc.respaldo /etc/bash.bashrc'" 
	    time.sleep(25)
	    print "Desinstalacion completada ---"
	    print "reinicie su pc"
	    self.exit()

	else:
	    print "cerrando el instalador"
	    self.exit()

    def exit(self):
	exit()
	exit()
	exit()
	  	
    def __init__(self):
	self.Presentacion()
	self.__del__()

    def __del__(self):
	print chr(27)+"[5;33m"+"FIN DEL PROGRAMA"
	os.system("exit")
	os.system("rm logs.txt")
	time.sleep(4)

if __name__ == "__main__":
    Instalador()
