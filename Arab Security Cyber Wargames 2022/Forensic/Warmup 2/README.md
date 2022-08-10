
#  Warm up 2
## Description

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/Arab%20Security%20Cyber%20Wargames%202022/Forensic/Warmup%202/Warmup%202%20.png)

## Solution
![enter image description here](https://github.com/vichhika/CTF-Writeup/blob/main/Arab%20Security%20Cyber%20Wargames%202022/Forensic/Warmup%202/warmup%202%20flag.png?raw=true)

using strings commend you will see the encoding text at top of the file. decode it using cyberchef you will get a plaintext and it is a reverse shell payload. sha1sum that ip address to get a flag.

The flag ASCWG{f778029a0c2cecd23e90986ca394952a5a770e8e}
