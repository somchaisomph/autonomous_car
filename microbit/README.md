โครงงานนี้ใช้ yotta ในการสร้างโปรแกรมสำหรับทำงานบน BBC-microbit หากท่านไม่คุ้นเคยกับการใช้งาน yotta สามารถศึกษาได้จาก https://goo.gl/7JdQbs
หน้าที่ของ BBC-microbit คือ เป็น remote control สำหรับบังคับ car โดยอาศัยข้อมูลจาก Bluetooth Service

<h2>การบังคับ</h2>
<ol>
<li><b>กดปุ่ม A </b>
<ol>
 <li>car ไปข้างหน้า</li>
 <li>กด long press เป็นการเร่งความเร็ว</li>
 </ol>
 </li>
 <li>
  
<b>กดปุ่ม B </b>
<ol>
 <li>car ถอยหลัง</li>
 <li>กด long press เป็นการเร่งความเร็ว</li>
 </ol>
 </li>
<li><b>กดปุ่ม A-B พร้อมกัน </b>
<ol>
 <li>ยุติการทำงาน</li>
 
 </ol>
</li>
  
<li>การเปลี่ยนแปลงค่าของ Accelerometer ในแนวแกน X เป็นการกำหนดทิศทางการลี้ยว
<img src="http://microbit-challenges.readthedocs.io/en/latest/_images/microbitAxes.jpg"/>
 <ul>
  <li>เอียงขวา = เลี้ยวขวา</li>
  <li>เอียงขวา = เลี้ยวซ้าย</li>
 </ul>
 </li>
 </ol>
<h2>ขั้นตอนการ compile</h2>
<ol>
  <li> สร้างโครงานตามขั้นตอนของ yotta</li>
  <li> สำเนา source/main.cpp ไปยัง  source ในโครงงานของท่าน</li>
  <li> สำเนา config.json ไปยังโครงงานของท่าน ให้อยู่ใน folder ระดับสุงสุดของโครงงาน </li>
  <li> yt clean <br/> 
       yt build</li>
</ol>
 <b>หมายเหตุ</b>
 ใน config.json ได้มีการกำหนดค่าให้ bluetooth.open = 1 ไว้ หมายถึง กำหนดให้ microbit สามารถติดต่อกับ Bluetooth อื่นได้โดยไม่ต้องผ่านขั้นตอนการ pair ในกรณีที่ไม่ต้องการข้ามขั้นตอนการ pair ให้กำหนด bluetooth.open = 0 ก่อนการ compile
