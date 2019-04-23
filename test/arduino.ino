int in1Pin = 6;      // back wheel 1
int in2Pin = 7;      // back wheel 2
int in3Pin = 8;      // front wheel 3
int in4Pin = 9;      // front wheel 4
int SpeedPin_34 = 2;    // front speed
int SpeedPin_12 = 3;    // back speed
int turn=0;



void setup() {
  Serial.begin(9600);
  Serial.setTimeout(30);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(SpeedPin_12, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  pinMode(SpeedPin_34, OUTPUT);
}
 
void loop() {
     ForwardM();   
     if(Serial.available()){ 
     turn = Serial.parseInt();
     FromRasp(turn);
    }   
}

void FromRasp(int turn)
{
  Serial.println(turn);
  switch(turn)
  {
    case 1:
      RightM(100);
      break;
    case 2:
      BigLeftM();
      break;
    case 3:
      LeftM(100);
      break;
    }
}

void ForwardM()
{
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  analogWrite(SpeedPin_12, 135);
}

void LeftM(int timed){
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, HIGH);
  analogWrite(SpeedPin_34, 200);
  delay(timed);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
}

void BigLeftM(){
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, HIGH);
  analogWrite(SpeedPin_34, 250);
  delay(500);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  analogWrite(SpeedPin_12, 250);
  delay(280);
}

void RightM(int timed){ 
  
  digitalWrite(in3Pin, HIGH);
  digitalWrite(in4Pin, LOW);
  analogWrite(SpeedPin_34, 200);
  delay(timed);   
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
}