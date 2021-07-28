# smrp-pi
Short Message Radiopacket Protocol for Raspberry Pi (3b)
Frequency Key Shifting experiment

SMRP-PI is a very simple FSK radio packet protocol for deliver short messages at about ~90 characters (ASCII/UTF-8) per minute. This experiment is more focused in some integrity instead of speed. 
This experiment takes advantage of "rpitx" project, which permits transmit radio using the PWM GPIO port of raspberry pi. 
This protocol is intended for transmit short-length information from weather stations, non-critical sensors, automatic digital signage updates, or some kind of notifications. The message is coded using generated square tones between 2 and 3000 Hz.

* LEGAL NOTE *

This software is intended for licensed amateur radio operators as a proof-of-concept and should not be used by anyone.
SMRP-PI uses "rpitx", a tool that transmit radio signals from PWM port of GPIO rpi. SQUARE radio signals ( = harmonics !!).
This means that your emission will be retransmitted in some (undesired) places of the spectrum, and this can lead a lot of problems! This is illegal and you will be in big troubles.
In the most countries around the world, it is illegal to transmit radio without license and/or appropiate equipment. RPI is NOT appropiate.
There is a lot of RPI hats to produce a legally tolerable emission for experimental/unlicensed bands (like ISM, 433 MHz, etc.). Buy some.
For experimental purposes, use a VERY small antenna ( less than 10 cms of copper cable ) and a band pass filter for a experimental and unlicensed band.
The transmit power of RPI (10 mW) is enough to create severe problems in a lot of devices. For security reasons, do not use this program on city environments, because you can interfere with pacemakers telemetry, electronic medical supplies, headphones, telephones, alarms, etc.
If you want to securely test, use some band pass filters and strong attenuators to connect directly the GPIO pin to SDR antenna in. It is the way I do. If you do not use attenuators, the signal is strong enough to burn your SDR hardware, so be careful.

HOW IT WORKS:

1) User types a message. 
2) The message is converted to hex.
3) The hex characters are converted to audio signals at specific frequencies to a wav file.
4) The WAV file is broadcasted (WFM) over radio (443 MHz and other ISM bands, be careful)
5) The receiver program detects the start tone, and listen for specific frequencies, which are translated to hex again.
7) The receiver calculates the first 3 digits of a md5 hash calculated from the message and compares it with the 3 digits received after the "separator" tone.
8) The end tone is received. If the checksums are equal, integrity is OK and the program shows the message.
7) Receiver program exits decrypter, and go idle again.

PACKET SCHEMA:

[START . . . . ] [MESSAGE ----- ] [SEPARATOR] [CHECKSUM (6 hex digits)] [END TONE . . .]

[START] The initialization variable is = 0 every 5 seconds. If a specific tone is detected in a sample, the variable gets + 1. When the variable is > 3 (4 samples with the same frequency, in a max time of 5 seconds) the program identifies that the next sequence will be a message.

[MESSAGE] Sucession of tones which are translated to HEX (2 characters HEX per character ASCII/UTF-8). Each letter are coded in this way:

  [ CHARACTER START TONE ] High-pitched tone. Needs > 3 samples to trigger.
  [ CHARACTER TONE ]  Medium-pitched tone for each character (alphabet: ABCDEF0123456789)
  [ SILENCE ] 2 Hz tone.  
  
[SEPARATOR] 

[CHECKSUM] This is a 6 digits (hex; corresponding to 3 ascii/utf-8 characters) checksum md5. For speed reasons, we only get the first 3 characters of the md5 hash, so virtually is possible a hash colission. 
