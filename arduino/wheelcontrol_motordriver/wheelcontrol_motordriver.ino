int in1Pin=6;
int in2Pin=7;
int in3Pin=8;
int in4Pin=9;
int echoPin=4;
int trigPin=5;

boolean bReverse=true; //뒷바퀴 제어
boolean FReverse=true; //앞바퀴 제어
int turn=0; //앞바퀴 방향

void setup() {
  Serial.begin(9600);
  pinMode(in1Pin,OUTPUT);
  pinMode(in2Pin,OUTPUT);
  pinMode(in3Pin,OUTPUT);
  pinMode(in4Pin,OUTPUT);
  pinMode(trigPin,OUTPUT);    //초음파 trig 출력모드
  pinMode(echoPin,INPUT);     //초음파 echo 입력모드
}

void loop() {
    float distance=ultrasonic(); //초음파 센서 거리
    
   if(distance<35) 
   {
      setMotor_b(bReverse);
      if(turn==0)   //핸들 방향 변경
      {
        FReverse=!FReverse;
        setMotor2(FReverse);
         turn=1;
       }
   }

   else
   {
    setMotor_f(bReverse);
    setMotor3(FReverse); 
    turn=0;
   }
}

float ultrasonic(void)  //초음파 거리 함수
{
  digitalWrite(trigPin,LOW);
  digitalWrite(echoPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  unsigned long duration=pulseIn(echoPin,HIGH); 
  float distance=((float)(340*duration)/10000)/2;
  return distance;
}

void setMotor_f(boolean bReverse)  //뒷바퀴 전진
{
  digitalWrite(in1Pin,!bReverse);
  digitalWrite(in2Pin,bReverse);
}

void setMotor_b(boolean bReverse)  //뒷바퀴 후진
{
  digitalWrite(in1Pin,bReverse);
  digitalWrite(in2Pin,!bReverse);
  delay(500);
}

void setMotor2(boolean FReverse)   //앞바퀴 왼쪽으로
{
  digitalWrite(in3Pin,!FReverse);
  digitalWrite(in4Pin,FReverse);
  delay(150);
}

void setMotor3(boolean FReverse)   //앞바퀴 오른쪽으로
{
  digitalWrite(in3Pin,FReverse);
  digitalWrite(in4Pin,!FReverse);
  delay(100);
}
