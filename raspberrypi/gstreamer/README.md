# การติดตั้ง
1. ใช้ install.sh ติดต้้ง gstreamer framework และ Python3 interface
2. ติดตั้ง Camera Module ตรวจสอบการทำงาน
3. เพิ่ม bcm2835-v4l2 เข้าไปใน /etc/modules แล้ว reboot เพื่อให้ gstreamer ติดต่อกับ Camera module ผ่านทาง /dev/video0
4. เรียกใช้ raspi_streamer.sh บน Raspberry Pi 
5. เรียกใช้ pc_viewer.sh บน PC (ต้องติดตั้ง gstreamer เช่นเดียวกัน)

***
[![DEMO](http://img.youtube.com/vi/pF1aIiK-m_8/0.jpg)](https://youtu.be/pF1aIiK-m_8)
