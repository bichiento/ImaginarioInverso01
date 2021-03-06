#define PIN_LED 13

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
    digitalWrite(PIN_LED, LOW);
  }


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




