from Services import BTService, UBitBtnService,AccelService
from Actors import GPIODriver,SteeringJob
from bluepy import btle
import Microbit as Ubit 



class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        
    def handleNotification(self,cHandle, data):
        global accel_serv,pi,steer
        x = 0
        pi.gpio_driver.write(6,1)
                
        if cHandle == accel_serv.cHandle :
            x,_,_ = accel_serv.get_data(data)
            steer.steer(x,pi.gpio_driver)
            
pi = GPIODriver()        
#need to assign bluetooth address of your own
ble_serv = BTService(peripheral_addr="XX:XX:XX:XX:XX")
steer = SteeringJob()
accel_serv = AccelService(Ubit.ACCEL_SRV,Ubit.ACCEL_DATA,Ubit.CCCD_UUID,ble_serv.device,Ubit.ACCEL_HANDLE)
ble_serv.set_delegate(MyDelegate())
accel_serv.start_notify(Ubit.START_NOTIFY_CODE)
while True : 
    ble_serv.notify(0.5)
accel_serv.stop_notify(Ubit.STOP_NOTIFY_CODE)
ble_serv.disconnect()
pi.stop()

    


 
 
