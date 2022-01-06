// Header files
#include <ArduinoJson.h>
#include <SPI.h>
#include <MFRC522.h>

// MFRC522 ss and rest pins
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

StaticJsonDocument<200> doc;

String card;
unsigned int ca = 0;
unsigned long int RFID_code = 0;
String data;


void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522

}


void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }

  String content= "";
  byte letter;
  String data = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     content = String(mfrc522.uid.uidByte[i], HEX);
     content.toUpperCase();
     ca = hexToDec(content);
     RFID_code = (RFID_code * 256) + ca;
  }

  String RFID = String(RFID_code);
 
  doc["ID"] = RFID;
  serializeJson(doc, data);
  Serial.println(data);
  delay(100);
}
 

// function to convert the hexadecimal to Decimal numbersystem
unsigned int hexToDec(String hexString) 
{
  
  unsigned int decValue = 0;
  int nextInt;
  
  for (int i = 0; i < hexString.length(); i++) 
  {
    nextInt = int(hexString.charAt(i));
    if (nextInt >= 48 && nextInt <= 57) nextInt = map(nextInt, 48, 57, 0, 9);
    if (nextInt >= 65 && nextInt <= 70) nextInt = map(nextInt, 65, 70, 10, 15);
    if (nextInt >= 97 && nextInt <= 102) nextInt = map(nextInt, 97, 102, 10, 15);
    nextInt = constrain(nextInt, 0, 15);
    
    decValue = (decValue * 16) + nextInt;
  }
  
  return decValue;
}
