# smrp-pi
SMRP-PI is a very simple radio packet protocol for deliver short messages at about ~90 characters per minute. This experiment is focused in find some reliability of the message (integrity) instead of speed.
This experiment takes advantage of "rpitx" project, which permits transmit radio using the PWM GPIO port of raspberry pi. 

PLEASE DO NOT TRANSMIT WITH YOUR RPI WITHOUT APPROPIATE FILTERS AND ATTENUATORS. For testing purposes, you can directly plug from RPI GPIO to SDR input using attenuators (connect it directly can damage your SDR hardware). 

1) User types a message. 
2) The message is converted to hex
3) The hex characters are converted to audio signals at specific frequencies to a wav file
4) The WAV file is broadcasted (WFM) over radio (443 MHz and other ISM bands, be careful)
5) The receiver program, using a SDR dongle, is idle and finds for a start tone.
6) A "end message" tone is received, and the HEX string is converted to ASCII/UTF-8 again. 
7) The receiver calculates the first 3 digits of a md5 hash calculated from the message and compares it with the 3 digits received after the "separator" tone.
8) If the checksums are equal, the message integrity is OK and the message is shown.
7) Receiver program exits decrypter, and go idle again finding a start tone. 

PACKET SCHEMA:

[START][MESSAGE][SEP][CHECKSUM][END]

[START] An XXXXX Hz tone that needs to fulfill a control variable for 4 samples in less than 5 seconds. If the variable is initialized, the program knows that a message is about to arrive.
[MESSAGE] Message in HEX (2 characters HEX per character ASCII/UTF-8)
[SEP] Separator tone.
[CHECKSUM] This is a 6 digits (hex; corresponding to 3 ascii/utf-8 characters) checksum md5. For speed reasons, we only get the first 3 characters of the md5 hash, so virtually is possible a hash colission. 
