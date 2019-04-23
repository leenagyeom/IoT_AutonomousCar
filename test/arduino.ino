int in3Pin = 8;      // front wheel 3
int in4Pin = 9;      // front wheel 4
int SpeedPin_34 = 5;    // front speed
int turn=0;
int numberLeft=0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(5);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  pinMode(SpeedPin_34, OUTPUT);
}

void loop() {
     if(Serial.available()){
     turn = Serial.parseInt();
     FromRasp(turn);
    }
}

void FromRasp(int turn)
{

  //Serial.println(turn);
  switch(turn)
  {
    case 1:
      RightM(80);
      break;
    case 2:
      if(numberLeft==3){
        numberLeft = 0;
        RightM(110);
      }
      else
        BigLeftM();
      break;
    case 3:
      LeftM();
      break;
    }
}

void LeftM(){
  digitalWrite(in3Pin, HIGH);
  digitalWrite(in4Pin, LOW);
  analogWrite(SpeedPin_34, 80);
  delay(50);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  delay(10);
}

void BigLeftM(){
  numberLeft++;
  digitalWrite(in3Pin, HIGH);
  digitalWrite(in4Pin, LOW);
  analogWrite(SpeedPin_34, 220);
  delay(700);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  delay(10);
}

void RightM(int tuurn){

  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, HIGH);
  analogWrite(SpeedPin_34, 200);
  delay(tuurn);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  delay(10);
}