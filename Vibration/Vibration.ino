int light = 3;   
int motor = 6;     
String input;    

void setup()
{
  Serial.begin(9600); 
  pinMode(motor, OUTPUT);
  pinMode(light, OUTPUT);

}
 
void loop()
{
  char buffer[16];
  if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    if (buffer[0] == 'Y') {
      digitalWrite(motor, HIGH);
    }
    if (buffer[0] == 'N') {
      digitalWrite(motor, LOW);
    }
}
}
