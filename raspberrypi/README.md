
# หน้าที่ของ Raspberry Pi
1. ควบคุมการหมุนของ Motor 
2. ควบคุมการเลีื้ยวผ่านการหมุน Servo
3. หน้าที่อื่น เช่น การถ่ายภาพ การ stream video
4. รับคำสั่งควบคุมจาก BBC microbit ผ่านทาง Bluetooth LE
***
# ติดตั้ง GPIO Driver
ในโครงงานนี้เลือกใช้ pigpio (http://abyz.me.uk/rpi/pigpio/pigpiod.html)

## การติดตั้ง
```
$ sudo apt-get install pigpio python3-pigpio
```


***
# ติดตั้ง Python Bluetooth LE interface
ทำการติดตั้ง bluepy ได้จากเว็บไซต์ https://github.com/IanHarvey/bluepy
