int enablePin = 11;
int in1Pin = 13;
int in2Pin = 12;
int echoPin = 8;
int trigPin = 9;
boolean bReverse = false;
int nSpeed = 200;

void setup()
{
  Serial.begin(9600);
  pinMode(enablePin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, OUTPUT);
}

void loop()
{
  digitalWrite(trigPin, LOW);
  digitalWrite(echoPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  unsigned long duration = pulseIn(echoPin, HIGH);
  float distance = ((float)(340*duration)/10000)/2;
  if (distance < 10)
  {
    bReverse = true;
  }
  else
  {
    bReverse = false;
  }
  setMotor(nSpeed, bReverse);
  Serial.print(distance);
  Serial.println("cm");
  delay(1000);
}

void setMotor(int nSpeed, boolean bReverse)
{
  analogWrite(enablePin, nSpeed);
  digitalWrite(in1Pin, !bReverse);
  digitalWrite(in2Pin, bReverse);
}
