#define PIN_LED 13
//conectar el arduino con transmisor al tx
//conectar el arduino con receptor al rx

byte msg[] = {
  'p', 'i', 'n', 'g', '\n'};
  
  // selecionar aleatoriamente de un archivo xml con el contenido del sitio un bloque 
  // de texto a partir de marcadores 

long long lastSendMillis;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(57600);
  lastSendMillis = millis();
}

void loop() {
  if(millis() > lastSendMillis+1000){
    lastSendMillis = millis();
    digitalWrite(PIN_LED, HIGH);
    Serial.write(msg, 5);
    digitalWrite(PIN_LED, LOW);
  }

// Imprimir el texto selecionado a la terminal 
// experar x cantidad de segundos deacuerdo al lenght 
//flush 

  if(Serial.available()){
    int rv = Serial.read();
    if(rv == 'p' || rv == 'n'){
      Serial.write(rv-32);
    }
    else if(rv == 'i'){
      Serial.write('O');
    }
    else if(rv == 'g'){
      Serial.write('G');
      Serial.write('\n');
    }
  }
}




