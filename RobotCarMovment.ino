#include<NewPing.h>

#define LT_R !digitalRead(10)
#define LT_M !digitalRead(4)
#define LT_L !digitalRead(2)

#define ENB 5
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
#define ENA 6

#define trigPin A5
#define echoPin A4

#define maxdistance 100
#define carSpeed 130


NewPing sonar(trigPin, echoPin, maxdistance); 

void forward() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go forward!");
}

void back() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("go back!");
}

void left() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go left!");
}

void right() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW); 
  Serial.println("go right!");
} 

void stop() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  Serial.println("Stop!");
} 

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(4, INPUT);
  pinMode(10, INPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void loop() {
   delay(70);
   int distance = sonar.ping_cm();
   if (distance == 0) {
    distance = 30;
   }
   if(distance <=15) {
    stop();
    delay(1000);
    left();
    delay(550);
    forward();
    delay(1000);
    right();
    delay(550);
    forward();
    delay(700);
    right();
    delay(550);
    forward();
    delay(600);
    left();
    delay(950);
    }
  if (LT_M) {
    forward();
  } else if (LT_R) {
    right();
  } else if (LT_L) {
    left();
  } else {
    stop();
    if (LT_M == 0 && LT_R == 0 && LT_L == 0) {
      delay(7500);
      forward();
    } 
    if (LT_M == 1 && LT_R == 0 && LT_L == 0){
      forward();
    }
   
  }
}
