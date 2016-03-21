#!/bin/bash
#/etc/init.d/bluetooth restart
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
rfcomm release rfcomm0
hcitool dev > log.txt | grep -e 'hci0' log.txt > mac.txt
cut -d "0" -f 2,3  mac.txt > MAC.txt
MAC=`cat MAC.txt`
echo "La mac del dispositivo es : $MAC"
hcitool scan > dispo.txt | grep -e "HC" dispo.txt > macd.txt
cut -d "H" -f  1  macd.txt > MACD.txt
#/etc/init.d/bluetooth status
#/etc/init.d/bluetooth force-reload
#/etc/init.d/bluetooth reset
rm log.txt mac.txt dispo.txt macd.txt
MACD=`cat MACD.txt`
echo "dispositivo HC-05 encontrado MAC: $MACD"
rfcomm connect -i $MACD 


