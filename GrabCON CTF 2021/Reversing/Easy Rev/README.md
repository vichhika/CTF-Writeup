# Easy Rev
## Description

Reverse Easy.....
## Solution
First we execute the binary
```bash
$ ./baby_re_2
Looking for the flag?
Enter the key: test
Wrong! Try Again ...
```
We try to analyze a binary to find the key using [ghidra](https://ghidra-sre.org/). We look up ``FUN_00101277`` function and we see some interest.
![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/Reversing/Easy%20Rev/figure_2.jpg)
First we look at ``line 19`` we show a condition that will execute another function. And we see ``local_20`` is an input variable and ``local_14`` variable that equal = ``0x140685``(Hex). Since the integer variable is readed as decimal so we try to convert the value of ``local_14`` to Decimal.
``140685 (Hex) = 1312389 (Decimal)``

So we found the key and we try to execute again
```bash
$ ./baby_re_2
Looking for the flag?
Enter the key: 1312389
GrabCON{y0u_g0t_it_8bb31}
```
We got flag!
