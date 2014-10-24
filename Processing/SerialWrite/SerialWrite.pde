// busca en un documento hml
// obtiene una frase
// imprime la frase en la terminal

import processing.serial.*;
Serial myPort; 
 
 
 String [] FrasesServidor = { loadXML text };
 String [] AutorFrase = { loadXML text };
 
 ArrayList ContenidoServidor;
 
 HashMap FraseCompleta;
 
 void setup(){
  FrasesCompletas = new HashMap<String, ArrayList>();
  ContenidoServidor = new ArrayList();
    String portName = Serial.list()[0];
    myPort = new Serial(this, portName, 9600);
    myPort.bufferUntil('\n');
 }
 
 
 void draw(){
 {
   

 void serialEvent(Serial myPort) {
 dataReading = myPort.readString();
 if(dataReading!=null){
    dataOutput = append(dataOutput, dataReading);
    saveData(); 
  } 
}
 
 
void printData() {
  myPort.write("saving to txt file...");
}
     
 
