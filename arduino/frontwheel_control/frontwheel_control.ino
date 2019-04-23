int enablePin = 11;
int in1Pin = 10;
int in2Pin = 9;
int switchPin = 7;



boolean bReverse = false;
int nSpeed = 250;
int now;
int turn = 0;



void setup() {
  Serial.begin(9600);
  pinMode(enablePin, OUTPUT);
  pinMode(in1Pin,OUTPUT);
  pinMode(in2Pin,OUTPUT);
  pinMode(switchPin, INPUT_PULLUP);
}



void loop() {
  //now = digitalRead(switchPin); //버튼을 연결해서 누를 때 방향을 틀게 한다면 주석을 풀고 now변수를 쓰면 된다.
  
  //if(now==0)
  //{

  
    if(turn%2==0)
    {
      setMotor(nSpeed, bReverse);
      setMotor2(nSpeed, !bReverse);
      turn++;
    }
    else
    {
      setMotor(nSpeed, !bReverse);
      setMotor2(nSpeed, bReverse);
      turn++;
    }

    
  //}

  delay(700);
}


void setMotor(int nSpeed, boolean bReverse)
{
  analogWrite(enablePin, nSpeed);
  digitalWrite(in1Pin, !bReverse);
  digitalWrite(in2Pin, bReverse);
  //delay(24); //RC카 말고 그냥 모터 선풍기에 테스트할 때 썼던 딜레이값
  delay(240); //방향을 튼 후에 너무 빠르게 돌아와서 눈에 보이지 않아서 방향전환 후 조금 더 머물도록 딜레이 길게 줌
  //analogWrite(enablePin, 0);
}


void setMotor2(int nSpeed, boolean bReverse)
{
  analogWrite(enablePin, nSpeed);
  digitalWrite(in1Pin, !bReverse);
  digitalWrite(in2Pin, bReverse);
  //delay(24);
  delay(40);
  analogWrite(enablePin, 0);
}
