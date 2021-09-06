
# Baby Rev
## Description

Baby Reverse.....
## Solution
First we execute the binary
```bash
$ ./baby_re_1
$
```
It didn't output anything. So let's try to disassemble a binary.
```bash
% objdump -d baby_re_1
....
....
0000000000001129 <main>:
    1129:       f3 0f 1e fa             endbr64
    112d:       55                      push   %rbp
    112e:       48 89 e5                mov    %rsp,%rbp
    1131:       c7 45 cc 8d df df 99    movl   $0x99dfdf8d,-0x34(%rbp)
    1138:       8b 45 cc                mov    -0x34(%rbp),%eax
    113b:       35 ef be ad de          xor    $0xdeadbeef,%eax
    1140:       89 45 d0                mov    %eax,-0x30(%rbp)
    1143:       c7 45 d4 94 f0 e2 9d    movl   $0x9de2f094,-0x2c(%rbp)
    114a:       8b 45 d4                mov    -0x2c(%rbp),%eax
    114d:       35 ef be ad de          xor    $0xdeadbeef,%eax
    1152:       89 45 d8                mov    %eax,-0x28(%rbp)
    1155:       48 b8 8b 8d df ac 30    movabs $0x7830acdf8d8b,%rax
    115c:       78 00 00
    115f:       48 89 45 e8             mov    %rax,-0x18(%rbp)
    1163:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    1167:       35 ef be ad de          xor    $0xdeadbeef,%eax
    116c:       89 45 dc                mov    %eax,-0x24(%rbp)
    116f:       48 b8 96 df da ea 5f    movabs $0x5feadadf96,%rax
    1176:       00 00 00
    1179:       48 89 45 f0             mov    %rax,-0x10(%rbp)
    117d:       48 8b 45 f0             mov    -0x10(%rbp),%rax
    1181:       35 ef be ad de          xor    $0xdeadbeef,%eax
    1186:       89 45 e0                mov    %eax,-0x20(%rbp)
    1189:       48 b8 df 8f cb b8 33    movabs $0x5f33b8cb8fdf,%rax
    1190:       5f 00 00
    1193:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    1197:       48 8b 45 f8             mov    -0x8(%rbp),%rax
    119b:       35 ef be ad de          xor    $0xdeadbeef,%eax
    11a0:       89 45 e4                mov    %eax,-0x1c(%rbp)
    11a3:       b8 00 00 00 00          mov    $0x0,%eax
    11a8:       5d                      pop    %rbp
    11a9:       c3                      ret
    11aa:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
....
....
```
Look! we see the code do something repeatly. Look at a sample once``address [ 1131-113b ]``, the hex value ``0x99dfdf8d`` was copied to the stack and stack was copied to the Accumulator register `%eax` to make **XOR** calcucate with ``0xdeadbeef``. So what output of these calculation? Is that a flag???

So we need to collect all these values above which did the calculation and make a simple python script to print out that results.
```python
xors = [ 0x99dfdf8d, 0x9de2f094, 0x7830acdf8d8b, 0x5feadadf96, 0x5f33b8cb8fdf]

[print(bytes.fromhex(hex(x^0xdeadbeef)[2:]).decode("ASCII"), end='') for x in xors]
```
**Code Explaination:**

 1. We store all the hex values that will calculate with ``0xdeadbeef``
 2. We do a loop to print out each of results but the output will be a decimal so we need to convert a decimal to hex to ASCII ( we want a text ).
```bash
ouput:
GrabCON{x0rr3d_4way_3ff10
```
We got flag!
