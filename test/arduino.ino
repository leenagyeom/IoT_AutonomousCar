int in1Pin = 6;      // �޹���
int in2Pin = 7;      // �޹���
int in3Pin = 8;      // �չ���
int in4Pin = 9;      // �չ���
int SpeedPin_F = 2;    // �չ��� �ӵ�
int SpeedPin_B = 3;    // �޹��� �ӵ�
int echoPin=4;		// ������
int trigPin=5;		// ������

void setup() {
	Serial.begin(9600);
	pinMode(in1Pin, OUTPUT);             // ���� 1���� ��¸�� ����
	pinMode(in2Pin, OUTPUT);             // ���� 2���� ��¸�� ����
	pinMode(SpeedPin_B, OUTPUT);            // PWM������ ��¸�� ����
	pinMode(in3Pin, OUTPUT);             // ���� 3���� ��¸�� ����
	pinMode(in4Pin, OUTPUT);             // ���� 4���� ��¸�� ����
	pinMode(SpeedPin_F, OUTPUT);            // PWM������ ��¸�� ����
	pinMode(trigPin,OUTPUT);
	pinMode(echoPin,INPUT);				// ������ ���;���
}

void loop() {
	// float distance=ultrasonic();

	//  Serial.println(distance);
	// if(distance<30)
	//   StopM();
	//  else
	ForwardM();

	if(Serial.available() > 0){			// ��������� ��ȣ������
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

	unsigned long duration = pulseIn(echoPin,HIGH);	// �������� high ������ �ð�(us) ���ϵ�
													// pulseIn(echoPin, High) pin�� �Է¸��, value�� ��Ʈ�� ���� ����
	float distance=((float)(340*duration)/10000)/2;	// high�ð����� �Ÿ� ��� (�����İ� �����ٰ� �ٽ� ���ƿ��� �ð�)
													// �պ��Ÿ��̹Ƿ� 2�� ������, ������ �ӵ��� 340m/s
													// duration�� ��(high ������ �ð�)�� us�����̹Ƿ� s������ �ٲ��ش�. (us -> s) duration / 10^6
													// 340m = 34000cm
													// �Ÿ�(cm) = (34000(cm/s) * duration(s) / 10^6)/2
													//            340*duration / 10000 / 2
	return distance;
} 

void ForwardM()
{
	digitalWrite(in1Pin, LOW);			//���Ͱ� ���������� ȸ��
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);		//���� �ӵ��� �ִ�� ����
}

void StopM()
{
	digitalWrite(in1Pin, LOW);			//���Ͱ� ���������� ȸ��
	digitalWrite(in2Pin, LOW);
	analogWrite(SpeedPin_B, 100);		//���� �ӵ��� �ִ�� ����
}

void LeftM(){
	digitalWrite(in1Pin, LOW);			//���Ͱ� ���������� ȸ��
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);
	digitalWrite(in3Pin, LOW);			//���Ͱ� ���������� ȸ��
	digitalWrite(in4Pin, HIGH);
	analogWrite(SpeedPin_F, 250);		// 250 : ���� ���� ũ��
	delay(1000);
}

void RightM(){
	digitalWrite(in1Pin, LOW);			//���Ͱ� ���������� ȸ��
	digitalWrite(in2Pin, HIGH);
	analogWrite(SpeedPin_B, 150);		// 150 : ���� ũ�� ������ �޸���
	digitalWrite(in3Pin, HIGH);			//���Ͱ� ���������� ȸ��
	digitalWrite(in4Pin, LOW);
	analogWrite(SpeedPin_F, 255);		// 255 : ���� ���� ũ��
	delay(1000);
}

void midM(){
	digitalWrite(in3Pin, LOW);			// �չ����� �� Ǯ���� (���� �߾����� ��ġ)
	digitalWrite(in4Pin, LOW);
	analogWrite(SpeedPin_F, 150);
}