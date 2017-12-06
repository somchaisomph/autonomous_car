from bluepy import btle
import Utils


class BTService():
    def __init__(self,peripheral_addr,addr_type=None):
        self.device = btle.Peripheral(peripheral_addr,btle.ADDR_TYPE_RANDOM)

    
    def set_delegate(self,delegate_class):
        try:
            self.device.setDelegate(delegate_class)
        except:
            pass
    
    def notify(self,dur=0.5):
        return self.device.waitForNotifications(dur)
    
    def disconnect(self):
        try :
            self.device.disconnect()
        except:
            pass
                    
    


class ServiceAbstrack():
    def __init__(self,serv_uuid,char_uuid,cccd_uuid,device,cHandle):
        self.service = None
        self.character = None
        self.descriptor = None
        self.data = {}
        self.cHandle = cHandle
    
    def get_data(self,raw_data):
        return None
    
    def start_notify(self,code):
        self.descriptor.write(code,False)
    
    def stop_notify(self,code):
        self.descriptor.write(code,False)
            
class UBitBtnService(ServiceAbstrack):
    def __init__(self,serv_uuid,char_uuid,cccd_uuid,device,cHandle):
        self.cHandle = cHandle
        self.service = device.getServiceByUUID(serv_uuid)
        self.character = self.service.getCharacteristics(char_uuid)[0]
        self.descriptor = self.character.getDescriptors(forUUID = cccd_uuid)[0]
    
    def get_data(self,raw_data):
        return (Utils.btn_decoder(raw_data) > 0)
    
        
class AccelService(ServiceAbstrack) :
    def __init__(self,serv_uuid,char_uuid,cccd_uuid,device,cHandle):
        self.cHandle = cHandle
        self.service = device.getServiceByUUID(serv_uuid)
        self.character = self.service.getCharacteristics(char_uuid)[0]
        self.descriptor = self.character.getDescriptors(forUUID = cccd_uuid)[0]
        
    def get_data(self,raw_data):
        x,y,z = Utils.accel_decoder(raw_data)
        return (x,y,z)
        
    
    
            

    
    
    
