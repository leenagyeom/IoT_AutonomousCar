int in1Pin = 6;      // 뒷바퀴
int in2Pin = 7;      // 뒷바퀴
int in3Pin = 8;      // 앞바퀴
int in4Pin = 9;      // 앞바퀴
int SpeedPin_F = 2;    // 앞바퀴 속도
int SpeedPin_B = 3;    // 뒷바퀴 속도
int echoPin=4;		// 초음파
int trigPin=5;		// 초음파

void setup() {
	Serial.begin(9600);
	pinMode(in1Pin, OUTPUT);             // 제어 1번핀 출력모드 설정
	pinMode(in2Pin, OUTPUT);             // 제어 2번핀 출력모드 설정
	pinMode(SpeedPin_B, OUTPUT);            // PWM제어핀 출력모드 설정
	pinMode(in3Pin, OUTPUT);             // 제어 3번핀 출력모드 설정
	pinMode(in4Pin, OUTPUT);             // 제어 4번핀 출력모드 설정
	pinMode(SpeedPin_F, OUTPUT);            // PWM제어핀 출력모드 설정
	pinMode(trigPin,OUTPUT);
	pinMode(echoPin,INPUT);				// 초음파 들어와야함
}

void loop() {
	// float distance=ultrasonic();

	//  Serial.println(distance);
	// if(distance<30)
	//   StopM();
	//  else
	ForwardM();

	if(Serial.available() > 0){			// 라즈베리에서 신호들어오면
		int turn = Serial.parseInt();
		Serial.println(turn);
		if(turn == 1)
		RightM();
		if(turn == 2)
		LeftM();
	}
	midM();

}

float ultrasonic(void)
{
	digitalWrite(trigPin,LOW);
	digitalWrite(echoPin,LOW);
	delayMicroseconds(2);
	digitalWrite(trigPin,HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin,LOW);

	unsigned long duration = pulseIn(echoPin,HIGH);	// 에코핀이 high 유지한 시간(us) 리턴됨
													// pulseIn(echoPin, High) pin은 입력모드, value는 포트의 레벨 지정
	float distance=((float)(340*duration)/10000)/2;	// high시간으로 거리 계산 (초음파가 나갔다가 다시 돌아오는 시간)
													// 왕복거리이므로 2로 나눈다, 초음파 속도는 340m/s
													// duration의 값(high 유지한 시간)은 us단위이므로 s단위로 바꿔준다. (us -> s) duration / 10^6
													// 340m = 34000cm
													// 거리(cm) = (34000(cm/s) * duration(s) / 10^6)/2
													//            340*duration / 10000 / 2
	return distance;
} 

void ForwardM()
{
	digitalWrite(in1Pin, LOW);			//모터가 정방향으로 회전
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);		//모터 속도를 최대로 설정
}

void StopM()
{
	digitalWrite(in1Pin, LOW);			//모터가 정방향으로 회전
	digitalWrite(in2Pin, LOW);
	analogWrite(SpeedPin_B, 100);		//모터 속도를 최대로 설정
}

void LeftM(){
	digitalWrite(in1Pin, LOW);			//모터가 정방향으로 회전
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);
	digitalWrite(in3Pin, LOW);			//모터가 정방향으로 회전
	digitalWrite(in4Pin, HIGH);
	analogWrite(SpeedPin_F, 250);		// 250 : 조향 각을 크게
	delay(1000);
}

void RightM(){
	digitalWrite(in1Pin, LOW);			//모터가 정방향으로 회전
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);		// 150 : 값이 크면 빠르게 달린다
	digitalWrite(in3Pin, HIGH);			//모터가 역방향으로 회전
	digitalWrite(in4Pin, LOW);
	analogWrite(SpeedPin_F, 255);		// 255 : 조향 각을 크게
	delay(1000);
}

void midM(){
	digitalWrite(in3Pin, LOW);			// 앞바퀴에 힘 풀려고 (축을 중앙으로 위치)
	digitalWrite(in4Pin, LOW);
	analogWrite(SpeedPin_F, 150);
}