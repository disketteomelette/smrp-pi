# -*- coding: utf-8 -*-

# IMPORTANTE: Este programa sólo genera un archivo WAV codificado (sampleaudio.wav). Ese archivo debe ser emitido usando rpitx para ser detectado.
# IMPORTANT: This program only generates a WAV file (sampleaudio.wav). You should transmit it using rpitx.

from pydub import AudioSegment
from pydub.generators import Square
from pydub.playback import play

s = "Hello world"
a = s.encode("hex")
s = a
print ("- Mensaje codificado:", s)
dura = 33
inicio = Square(3000).to_audio_segment(duration=90)

# CARACTERES ESPECIALES
tonoinicio = Square(300).to_audio_segment(duration=dura)
tonofinal = Square(200).to_audio_segment(duration=dura)
tonoseparador = Square(2300).to_audio_segment(duration=dura)

# A
tono1 = Square(400).to_audio_segment(duration=dura)
# B
tono2 = Square(500).to_audio_segment(duration=dura)
# C
tono3 = Square(600).to_audio_segment(duration=dura)
# D
tono4 = Square(700).to_audio_segment(duration=dura)
# E
tono5 = Square(800).to_audio_segment(duration=dura)
# F
tono6 = Square(900).to_audio_segment(duration=dura)
# 1
tono7 = Square(970).to_audio_segment(duration=dura)
# 2
tono8 = Square(1080).to_audio_segment(duration=dura)
# 3
tono9 = Square(1180).to_audio_segment(duration=dura)
# 4
tono10 = Square(1300).to_audio_segment(duration=dura)
# 5
tono11 = Square(1400).to_audio_segment(duration=dura)
# 6
tono12 = Square(1500).to_audio_segment(duration=dura)
# 7
tono13 = Square(1600).to_audio_segment(duration=dura)
# 8
tono14 = Square(1700).to_audio_segment(duration=dura)
# 9
tono15 = Square(1800).to_audio_segment(duration=dura)
# 0
tono16 = Square(1900).to_audio_segment(duration=dura)
# Silencio
silencio = Square(1).to_audio_segment(duration=100)
# Inicializamos con silencio para evitar que el detector se vuelva loco
resultado = silencio

for c in s :

    if "a" in c : tono = tono1
    if "b" in c : tono = tono2
    if "c" in c : tono = tono3
    if "d" in c : tono = tono4
    if "e" in c : tono = tono5
    if "f" in c : tono = tono6
    if "1" in c : tono = tono7
    if "2" in c : tono = tono8
    if "3" in c : tono = tono9
    if "4" in c : tono = tono10
    if "5" in c : tono = tono11
    if "6" in c : tono = tono12
    if "7" in c : tono = tono13
    if "8" in c : tono = tono14
    if "9" in c : tono = tono15
    if "0" in c : tono = tono16

    # dentro del for:
    # inicio - tono actual - silencio

    inicio = inicio.append(inicio, crossfade=5).append(tono, crossfade=5).append(silencio, crossfade=5)

# fuera del for:
# tonoinicio - (resultado) - tonofinal

# Generamos el archivo que será emitido
inicio.export("sampleaudio.wav", format="wav")


