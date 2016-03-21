// Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
// los terminos de la licencia pública general de GNU, según es publicada 
// por la free software fundation bien la versión 3 de la misma licencia 
//o de cualquier versión posterior. (según su elección ).
// Si usted hace alguna modificación en esta aplicación, deberá siempre
// mencionar el autor original de la misma.
// Autor: 
// Universidad  Distrital Francisco Jose  
// Grupo de fisica e informatica
// Diego Alberto Parra Garzón 
// Dr Julian Andres Salamanca Bernal
// Colombia, Bogota D.C.
#include "Arduino.h"
void setup();
void Velo0();
void Velo1();
void Velo2();
void Velo3();
void Velo4();
void Velo5();
void Velo6();
void Vepa1();
void Vepa2();
void Vepa3();
void Vepa4();
void Vepa5();
void Inten1();
void Inten2();
void inicio();
void Menu();
void loop();
#line 1
int motor = 3;
const int sensor1 = A0;
const int sensor2 = A5;
const int ledRojo = 12;
const int ledAzul = 9;
const int ledVerde = 10;
const int ledEmisor = 6;
//const int resetea = 4;
//variables
long miliVolts1;
long intensidad1;
int brillo1;


void setup()
{
  Serial.begin(9600);
  pinMode(ledAzul, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledEmisor, OUTPUT);
//  pinMode(resetea, OUTPUT);
}

void Velo0()
{
      //int  velocidad = map(velocidad,'0', '5', 0, 255);
      //velocidad = 0;
      //analogWrite(motor, velocidad);
      analogWrite(motor, 0);
      delay(20);
}

void Velo1()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '150';
      //analogWrite(motor, velocidad);
       analogWrite(motor, 135);
      //delay(20);
}

void Velo2()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '160';
      //analogWrite(motor, velocidad);
      analogWrite(motor, 140);
      //delay(20);
}

void Velo3()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '170';
      //analogWrite(motor, velocidad);
      analogWrite(motor, 145);
      //delay(20);
}

void Velo4()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '180';
      //analogWrite(motor, velocidad);
      analogWrite(motor, 150);
      //delay(20);
}

void Velo5()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '190';
      //analogWrite(motor, velocidad);
       analogWrite(motor, 160);
      //delay(20);
}

void Velo6()
{
      //int  velocidad = map(velocidad,'0', '255', 0, 255);
      //velocidad = '200';
      //analogWrite(motor, velocidad);
       analogWrite(motor, 190);
//      delay(20);
}

void Vepa1()
{
  analogWrite(motor, 150);
  delay(55);
  Velo0();
  delay(1000);
 // digitalWrite(resetea, HIGH);
 
}

void Vepa2()
{
  analogWrite(motor, 150);
  delay(50);
  Velo0();
  delay(1000);
}

void Vepa3()
{
  analogWrite(motor, 150);
  delay(45);
  Velo0();
  delay(1000);
}

void Vepa4()
{
  analogWrite(motor, 150);
  delay(40);
  Velo0();
  delay(1000);
}

void Vepa5()
{
  analogWrite(motor, 150);
  delay(37);
  Velo0();
  delay(1000);
}

void Inten1()  
{
  miliVolts1 = ((analogRead(sensor1) *5000L) /1023)*4; //opteniendo el valor sensor
  intensidad1 =miliVolts1;
  brillo1 = map(intensidad1, 0, 5000, 0, 255); //funcion map (mapeo) convierte la variable y le da un rango y un dominio
  brillo1 = constrain(brillo1, 0, 255); //funcion constrain o contenido en el intervalo de analogWrite (0, 255)
  analogWrite(ledAzul, 255 - brillo1 );   //Salida del led si esta el obstaculo esta lejos
  analogWrite(ledVerde, brillo1); //Salida del led si el obstaculo esta cerca
  Serial.print(" "); //salida al Serialporth
  Serial.print(intensidad1);
  Serial.println(" ");
  delay (3);
}

void Inten2()
{
  miliVolts1 = ((analogRead(sensor2) *5000L) /(1023))*4; //opteniendo el valor sensor
  intensidad1 =miliVolts1;
  brillo1 = map(intensidad1, 0, 5000, 0, 255); //funcion map (mapeo) convierte la variable y le da un rango y un dominio
  brillo1 = constrain(brillo1, 0, 255); //funcion constrain o contenido en el intervalo de analogWrite (0, 255)
  analogWrite(ledEmisor,   255);
  analogWrite(ledAzul, 255-brillo1 ); //Salida del led si esta el obstaculo esta lejos
  analogWrite(ledVerde, brillo1); //Salida del led si el obstaculo esta cerca
  Serial.print(" "); //salida al Serialport
  Serial.print(intensidad1);
  Serial.println(" ");
  delay (3);
}

//void resetear()
  //{
    //digitalWrite(resetea, HIGH);
    //delay(150);
    //digitalWrite(resetea, LOW);
    //delay(150);
  //}
  
void inicio()
{
  digitalWrite(ledRojo, HIGH);   // turn the LED on (HIGH is the voltage level)
  analogWrite(ledAzul, 255);
  analogWrite(ledVerde, 255);
  delay(100);               // wait for a second
  analogWrite(ledRojo, LOW);    // turn the LED off by making the voltage LOW
  analogWrite(ledAzul, 255);
  analogWrite(ledVerde, 255);
  delay(100);
}

void Menu()
{
  
  char opcion = Serial.read();
  switch (opcion )
  {
    case 'a': 
            
              
              while(opcion=='a')
              {
                inicio();
                Velo0();
                Menu();              
              }
              break;
              
      case 'b': 
            
              
              while(opcion=='b')
              {
                inicio();
                Velo1();
                Menu();              
              }
              break;
              
      case 'c': 
             while(opcion=='b')
              {
                inicio();
                Velo2();
                Menu();              
              }
              break;
 
     case 'd': 
            while(opcion=='d')
              {
                inicio();
                Velo3();
                Menu();              
              }
              break;
              
      case 'e': 
              while(opcion=='e')
              {
                inicio();
                Velo4();
                Menu();              
              }
              break;
              
      case 'f': 
              while(opcion=='f')
              {
                inicio();
                Velo5();
                Menu();              
              }
              break;
 
      case 'g': 
              while(opcion=='g')
              {
                inicio();
                Velo6();
                Menu();              
              }
              break;
              
      case 'h': 
              while(opcion=='h')
              {
                Velo0();
                Inten1();
                Menu();              
              }
              break;
              
      case 'i': 
              while(opcion=='i')
              {
                Velo1();
                Inten1();
                Menu();              
              }
              break;
 
     case 'j': 
            while(opcion=='j')
              {
                Velo2();
                Inten1();
                Menu();              
              }
              break;
              
      case 'k':
                
              while(opcion=='k')
              {
                Velo3();
                Inten1();
                Menu();             
              }
              break;
              
      case 'l': 
              while(opcion=='l')
              {
                Velo4();
                Inten1();
                Menu();              
              }
              break;
       
       case 'm': 
              while(opcion=='m')
              {
                Velo5();
                Inten1();
                Menu();              
              }
              break;
              
      case 'n': 
              while(opcion=='n')
              {
                Velo6();
                Inten1();
                Menu();              
              }
              break;
 
     case 'z': 
            while(opcion=='z')
              {
                Velo0();
                Inten2();
                Menu();              
              }
              break;
              
      case 'o': 
              while(opcion=='o')
              {
                Velo1();
                Inten2();
                Menu();              
              }
              break;
              
      case 'p': 
              while(opcion=='p')
              {
                Velo2();
                Inten2();
                Menu();              
              }
              break;
 
    case 'q': 
            while(opcion=='q')
              {
                Velo3();
                Inten2();
                Menu();              
              }
              break;
              
      case 'r': 
              while(opcion=='r')
              {
                Velo4();
                Inten2();
                Menu();              
              }
              break;
              
      case 's': 
              while(opcion=='s')
              {
                Velo5();
                Inten2();
                Menu();              
              }
              break; 
              
      case 't': 
              while(opcion=='t')
              {
                Velo6();
                Inten2();
                Menu();              
              }
              break; 
     //case 'u':
       //        { 
         //        resetear();
           //      Menu();
             //  }
              // break;
               
     case '1':
               {
                 Vepa1();
                 Menu();
               }
               break;
  
     case '2':
              {
                Vepa2();
                Menu();
               }
               break;
    case '3':
              {
                Vepa3();
                Menu();
               }
               break;
    case '4':
              {
                Vepa4();
                Menu();
               }
               break;
    case '5':
              {
                Vepa5();
                Menu();
               }
               break;
   }
  
}

void loop()
{
  
  inicio();
  Menu();
    
}

