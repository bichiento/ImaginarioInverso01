
// abrir la terminal y escribir 
// ls /dev/tty.* en la terminal para ver el nombre del puerto
// screen /dev/tty.usbmodemfa131 9600 para transmitir 
// screen /dev/tty.usbmodemfa121 9600 para recivir 


#include <SoftwareSerial.h>

SoftwareSerial mySerial(0, 1); // RX, TX

void setup()  
{
  Serial.begin(9600);
  while (!Serial) {
    ;
  }


  Serial.println("Bienvenidos a CODEPI!");
  mySerial.begin(9600);
  //Serial.println("CODEPI DICE"); el que recibe 
}

void loop()                     
{

if (mySerial.available()) {
Serial.print((char)mySerial.read());
}
if (Serial.available()) {
mySerial.print((char)Serial.read());
}
//delay(1000);
}
