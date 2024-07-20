#include <Servo.h>

Servo S1;
Servo E1;
Servo E2;
Servo S2;

int in3=9;
int in4=11;




byte val = "";


void setup(){
  E1.attach(4);
  S1.attach(5);
  E2.attach(2);
  S2.attach(3);
  Serial.begin(9600); 
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);



}
void hi(){
  E1.write(0);
  delay(100);
  S1.write(180);
  
  delay(850);
  S1.write(90);
  
  delay(1500);
  S1.write(0); 
  delay(580);
  E1.write(90);
  S1.write(90);
  delay(50);
  S1.write(180);
  delay(50);
  S1.write(90);


   
}
void bye(){
  E1.write(0);
  delay(100);
  S1.write(180);
  
  delay(600);
  S1.write(90);

  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  delay(2000);
  digitalWrite(in4,HIGH);
  digitalWrite(in3,LOW);
  delay(2000);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  delay(2000);
  digitalWrite(in4,HIGH);
  digitalWrite(in3,LOW);
  delay(2000);
  digitalWrite(in4,LOW);
  digitalWrite(in3,LOW);

  S1.write(0); 
  delay(500);
  E1.write(90);
  S1.write(90);
  delay(50);
  S1.write(180);
  delay(50);
  S1.write(90);
}

void explain(){
  E1.write(0);
  delay(500);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  delay(2000);
  digitalWrite(in4,HIGH);
  digitalWrite(in3,LOW);
  delay(2000);
  digitalWrite(in4,LOW);
  digitalWrite(in3,LOW);

  E1.write(90);
  delay(1000);
  S2.write(45);
  delay(700);
  S2.write(90);
  delay(10);
  S2.write(135);
  delay(700);
  S2.write(90);


}


void hand_up(){
  delay(1500);
  E1.write(0);
  E2.write(180);
  delay(1500);
  E1.write(90);
  E2.write(90);

}


void loop() {
  // put your main code here, to run repeatedly:
  

  while(Serial.available() > 0)  //look for serial data available or not
 
  {
    val = Serial.read();        //read the serial value

    if(val == 'h'){
      // do hi
       hi();
    }
    if(val == 'g'){
      bye();
    }
    if(val == 'z'){
      hand_up();
    }
    
    
    
  }
}


