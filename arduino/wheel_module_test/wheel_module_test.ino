int enablePin=11;
int enablePin2=5;
int in1Pin=13;
int in2Pin=12;
int in3Pin=7;
int in4Pin=6;
int echoPin=8;
int trigPin=9;



boolean bReverse=false; //뒷바퀴 제어
boolean FReverse=true; //앞바퀴 제어
int nSpeed=255; //뒷바퀴 속도
int FSpeed=250; //앞바퀴 속도
int turn=0; //앞바퀴 방향



void setup() {
  Serial.begin(9600);
  pinMode(enablePin,OUTPUT);  //뒷바퀴꺼
  pinMode(enablePin2,OUTPUT); //앞바퀴꺼
  pinMode(in1Pin,OUTPUT);
  pinMode(in2Pin,OUTPUT);
  pinMode(in3Pin,OUTPUT);
  pinMode(in4Pin,OUTPUT);
  pinMode(trigPin,OUTPUT);    //초음파 trig 출력모드
  pinMode(echoPin,INPUT);     //초음파 echo 입력모드
}



void loop() {

  float distance=ultrasonic(); //초음파 센서 거리

   if(distance<10)    //거리가 10이하면 속도 감소해서 정지
   {
      while(nSpeed>80)
        nSpeed-=2;
      if(turn==0)   //핸들 방향 변경
      {
        FReverse=!FReverse;
        setMotor2(FSpeed,FReverse);
        delay(500);
        setMotor3(FSpeed,FReverse);
         turn=1;
       }
   }
   else   //아니면 최고 속도
   {
    bReverse=false;
    while(nSpeed<255)
      nSpeed+=2;
    turn=0;
   }
   setMotor(nSpeed,bReverse);
   delay(700);
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



void setMotor(int nSpeed,boolean bReverse)  //뒷바퀴 방향 함수
{
  analogWrite(enablePin,nSpeed);
  digitalWrite(in1Pin,!bReverse);
  digitalWrite(in2Pin,bReverse);
  delay(240);
}



void setMotor2(int FSpeed,boolean FReverse)   //앞바퀴 왼쪽으로
{
  analogWrite(enablePin2,FSpeed);
  digitalWrite(in3Pin,!FReverse);
  digitalWrite(in4Pin,FReverse);
  delay(150);
}

void setMotor3(int FSpeed,boolean FReverse)   //앞바퀴 오른쪽으로
{
  analogWrite(enablePin2,FSpeed);
  digitalWrite(in3Pin,FReverse);
  digitalWrite(in4Pin,!FReverse);
  delay(100);
  analogWrite(enablePin2,0);
