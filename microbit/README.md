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
  <li> สำเนา source/main.cpp ไปยังโครงงานของท่าน </li>
  <li> สำเนา config.json ไปยังโครงงานของท่าน </li>
  <li> yt clean ตามด้วย yt build</li>
</ol>
  
