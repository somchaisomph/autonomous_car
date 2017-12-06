#include "MicroBit.h"

MicroBit uBit;
uint8_t connected = 0;

void onBTConnected(MicroBitEvent){
	connected = 1;
	uBit.display.print("C");
}
void onBTDisconnected(MicroBitEvent){
	connected = 0;
	uBit.display.print("D");
}

int main(){
	uBit.init();
	/*** Let listen to the world ***/
	uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onBTConnected);
	uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onBTDisconnected);
	
	/*** Start Bluetooth services ***/
	new MicroBitAccelerometerService(*uBit.ble, uBit.accelerometer);
    new MicroBitMagnetometerService(*uBit.ble, uBit.compass);
    new MicroBitButtonService(*uBit.ble);
    
	release_fiber();
}
