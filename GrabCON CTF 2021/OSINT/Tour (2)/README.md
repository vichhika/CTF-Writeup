# Tour (2)
## Description

Can you find the flight number and the flight operator of the last flight that took her to the final destination?

E.g. GrabCON{AF226_Air_France}

required to solve [The Tour (1)](https://github.com/vichhika/CTF-Writeup/blob/main/GrabCON%20CTF%202021/OSINT/The%20Tour%281%29/README.md) first.

## Solution
From the previous task  "[The Tour (1)](https://github.com/vichhika/CTF-Writeup/blob/main/GrabCON%20CTF%202021/OSINT/The%20Tour%281%29/README.md)" , we see some interest clue : ``airline ticket`` and  ``the car that came to the airport to receive her``

Investigation :
 1. What is `Let's go! CAMPER` which is on the car?
 2. The barcode was leaked on that ``airline ticket`` picture so what that barcode is about?

So now we try to find ``Let's go! CAMPER`` and we get their [website](https://www.letsgocamper.com/).

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/OSINT/Tour%20%282%29/figure_1.jpg)

We can define her ``airline ticket`` now. The last location that she have a food is at ``Serbia`` and the car that came to the airport to receive her is in ``Antalya, Turkey`` . So it means that she fly from ``Serbia`` to ``Turkey``. Here is an serbia ticket example:

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/OSINT/Tour%20%282%29/figure_2.jpg)

Look at the example once, The ticket is very similar to her ticket. So We can detect that:

 1. Her flight operator is : ``AirSERBIA``
 2. Flight No : ``JU XXXX``

How we find Flight Number?

First we try find the type of barcode.

![enter image description here](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/OSINT/Tour%20%282%29/figure_3.jpg)

We see that it's a ``PDF417 barcode`` which according to [IATA (wiki)](https://en.wikipedia.org/wiki/International_Air_Transport_Association) standard. Easier way, we use [online tool](https://online-barcode-reader.inliteresearch.com/) to read the barcode.

![https://online-barcode-reader.inliteresearch.com/](https://raw.githubusercontent.com/vichhika/CTF-Writeup/main/GrabCON%20CTF%202021/OSINT/Tour%20%282%29/figure_4.jpg)

Look at the result, we can detect a pattern which look like Flight No. but what is ``BEGIST`` which stand before ``JU 0802``? Base on [IATA's code search](https://www.iata.org/en/publications/directories/code-search/):

 - the 2-letter code of an airline or identify to which airline a 2-letter code corresponds
 - the 3-letter code of an airport location or identify which airport uses a particular code

So ``BEGIST`` which means Origin to Destination. We can find the 3-letter code using this [airport code list](https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm):

``BEG`` = [Belgrad](https://www.nationsonline.org/oneworld/map/google_map_Belgrade.htm) (Beograd) - Belgrade Nikola Tesla International
``IST`` = [Istanbul](https://www.nationsonline.org/oneworld/map/google_map_Istanbul.htm) - Istanbul Atatürk Airport

Let's merge our info to get a flag base on example flag in description above:

 1. [JU 0802](https://www.google.com/search?q=JU%200802) = ``JU802``
 2. AirSerbia = ``Air_Serbia``

flag = ``GrabCON{JU802_Air_Serbia}``

Learn more : [What’s contained in a boarding pass barcode?](https://shaun.net/notes/whats-contained-in-a-boarding-pass-barcode/)
