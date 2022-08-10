
#  Warm up 2
## Description

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/Arab%20Security%20Cyber%20Wargames%202022/Forensic/Weird%20Fs/Weird%20Fs%20.png)

## Solution
![enter image description here](https://cdn.discordapp.com/attachments/1005119061031649370/1006882974702252032/unknown.png)

First, try to identify the type of file. Why it look so wire. Why I can't open just double click.
So we know it an **Apple APFS**.

![enter image description here](https://cdn.discordapp.com/attachments/1005119061031649370/1005153330982572062/unknown.png)

So we using [apfs-fuse](https://github.com/sgan81/apfs-fuse) tool to mount this img into the folder. After we mounted it, we will see all the files inside that folder. I notice Flag.zip file. So I try to copy to outside and open but it has a password.

There are 2 ways to solved this:
	1. Brute force
	2. Keep finding any clue relate to credential in that mount folder.

So I try to crack it using john while dicovering inside that folder then I got its password: **juelma**
pwn! we got flag.
