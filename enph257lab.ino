
int sensePin0 = A0;  // This is the Arduino Pin that will read the sensor output
int sensePin1 = A1;  // This is the Arduino Pin that will read the sensor output
int sensePin2 = A2;  // This is the Arduino Pin that will read the sensor output
int sensePin3 = A3;  // This is the Arduino Pin that will read the sensor output
int sensePin4 = A4;  // This is the Arduino Pin that will read the sensor output 

int sensorInput;     // The variable we will use to store the sensor input
double temp0, temp1, temp2, temp3, temp4;     // The variable we will use to store temperature in degrees.

void setup() {
  Serial.begin(9600); // Start the Serial Port at 9600 baud (default)
}

void loop() {
  temp0 = returnTemp(sensePin0);
  temp1 = returnTemp(sensePin1);
  temp2 = returnTemp(sensePin2);
  temp3 = returnTemp(sensePin3);
  temp4 = returnTemp(sensePin4);

  Serial.print("Sensor 0 Temperature: ");
  Serial.print(temp0);
  
  Serial.print("Sensor 1 Temperature: ");
  Serial.print(temp1);
  
  Serial.print("Sensor 2 Temperature: ");
  Serial.print(temp2);
  
  Serial.print("Sensor 3 Temperature: ");
  Serial.print(temp3);

  Serial.print("Sensor 4 Temperature: ");
  Serial.print(temp4);
  delay(750);
}

double returnTemp(int address) {
  sensorInput = analogRead(address);   // Read the analog sensor and store it
  temp = (double)sensorInput / 1024;   // Find percentage of input reading
  temp = temp * 5;                     // Multiply by 5V to get voltage
  temp = temp - 0.5;                   // Subtract the offset 
  temp = temp * 100;                   // Convert to degrees 
  return temp;
}

