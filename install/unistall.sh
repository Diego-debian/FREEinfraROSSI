#!/bin/bash
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad Distrital Francisco Jose  
# Grupo de fisica e informatica
# Diego Alberto Parra Garzón 
# Dr Julian Andres Salamanca Bernal
# Colombia, Bogota D.C.

cp /etc/bash.bashrc /etc/bash.bashrc.respaldo
rm -rf ~/Documentos/Free-infrarossi
cat /etc/bash.bashrc | grep -n "infrarossi" | cut -d ":" -f 1,1  > logs.txt
NUM=`cat logs.txt`
LET=`echo d`
LINEA=`echo -e "$NUM$LET"`
sed -i "$LINEA" /etc/bash.bashrc 
