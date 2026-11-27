#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"
#include "Adafruit_SHT31.h"

Adafruit_BME680 bme;                 // I2C
Adafruit_SHT31  sht = Adafruit_SHT31();
const int BTN = 0;                   // BOOT button = breath marker

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);                // SDA = GPIO21, SCL = GPIO22
  if (!bme.begin(0x77) && !bme.begin(0x76)) { Serial.println("# BME688 not found"); while (1) delay(10); }
  if (!sht.begin(0x44)) { Serial.println("# SHT31 not found"); while (1) delay(10); }
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150);        // 320 C for 150 ms
  pinMode(BTN, INPUT_PULLUP);
  Serial.println("time_ms,T_sht,RH_sht,T_bme,RH_bme,P_bme,gas_ohm,marker");
}

void loop() {
  unsigned long t = millis();
  int marker = (digitalRead(BTN) == LOW) ? 1 : 0;
  if (!bme.performReading()) { Serial.println("# read failed"); return; }
  float ts = sht.readTemperature();
  float rh = sht.readHumidity();
  Serial.printf("%lu,%.2f,%.2f,%.2f,%.2f,%.2f,%lu,%d\n", t, ts, rh,
                bme.temperature, bme.humidity, bme.pressure / 100.0,
                (unsigned long)bme.gas_resistance, marker);
  while (millis() - t < 1000) delay(5);   // one row per second
}
