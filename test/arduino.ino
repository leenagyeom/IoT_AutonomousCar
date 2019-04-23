int in1Pin = 6;      // back wheel 1
int in2Pin = 7;      // back wheel 2
int in3Pin = 8;      // front wheel 3
int in4Pin = 9;      // front wheel 4
int SpeedPin_34 = 2;    // front speed
int SpeedPin_12 = 3;    // back speed
int turn=0;

void setup() {
  Serial.begin(9600);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(SpeedPin_12, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  pinMode(SpeedPin_34, OUTPUT);
}
 
void loop() {
     ForwardM();
    
    if(Serial.available() > 0){ 
      turn = Serial.parseInt();
      Serial.println(turn);
      if(turn == 1 | turn == 11){
          RightM(300);
          midM();
      }
      if(turn == 2 | turn == 22){
          LeftM(1000);
          midM();
      }
    }   
}

void ForwardM()
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);
  analogWrite(SpeedPin_12, 120);
}

void LeftM(int timed){
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, HIGH);
  analogWrite(SpeedPin_34, 250);
  delay(timed);
}

void RightM(int timed){ 
  
  digitalWrite(in3Pin, HIGH);
  digitalWrite(in4Pin, LOW);
  analogWrite(SpeedPin_34, 250);
  delay(timed);   
}

void midM(){
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  analogWrite(SpeedPin_34, 250);
}