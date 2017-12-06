import subprocess

def accel_decoder(val):
    '''
    accept input in bytes with lenght of 6
    then split out and convert to integer
    '''
    x = int.from_bytes(val[0:2],byteorder='little',signed=True)
    y = int.from_bytes(val[2:4],byteorder='little',signed=True)
    z = int.from_bytes(val[4:6],byteorder='little',signed=True)
    return [x/1000,y/1000,z/1000]

def btn_decoder(val):
    return int.from_bytes(val,byteorder='little', signed=False)
    
def get_ble_mac():
	
	proc = subprocess.Popen(["hcitool","dev"],stdout=subprocess.PIPE)
	cli = proc.communicate() # cli[0] = ble mac address
	ble_mac = cli[0].decode("utf-8")
	if len(ble_mac) < 17 : 
		return None
	else :
		return ble_mac[-17:]

def turn_ble_on():
	#unblock rfkill
	try:
		subprocess.call(["sudo","rfkill","unblock","bluetooth"])
		subprocess.call(["sudo","hciconfig","hci0","up"])
	except :
		pass
	return True
	
	
	
