import pyaudio
import wave
import sys
import struct
import math
import numpy as np
import os

# IMPORTANTE: Es necesario configurar adecuadamente el cable virtual. Un microfono puede dar resultados inesperados.
# IMPORTANT: You have to configure properly a virtual cable. A microphone can lead to unexpected results.

# Constantes
TOLERANCE = 50
THRESH = 0.1
N = 10

def rms (data) :
    count = len(data) / 2
    format = "%dh" % (count)
    shorts = struct.unpack(format, data)
    sum_squares = 0.0
    for sample in shorts :
        n = sample * (1.0 / 32768)
        sum_squares += n * n
    return math.sqrt(sum_squares / count)


def listen () :
    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 60
    AUDIO_INDEX = 2
    contador = 0
    mensaje = ""

    window = np.blackman(CHUNK)
    swidth = 2

    past = [-1] * N
    command = []
    active = False

    p = pyaudio.PyAudio()

    audio_in = p.get_device_info_by_index(AUDIO_INDEX)
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=audio_in['index'])

    # DEBUG: para mostrar informacion de la entrada de audio seleccionada:
    # print(audio_in)

    mensajein = muestra = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)) :
        data = stream.read(int(CHUNK / 2))
        indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), \
                                             data)) * window
        fftData = abs(np.fft.rfft(indata)) ** 2
        # buscando el pico máximo
        which = fftData[1 :].argmax() + 1
        if which != len(fftData) - 1 :
            y0, y1, y2 = np.log(fftData[which - 1 :which + 2 :])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            frecuenciaestimada = (which + x1) * RATE / CHUNK
        else :
            frecuenciaestimada = which * RATE / CHUNK
        frecuenciaestimada = frecuenciaestimada * 2
        muestra = muestra + 1
        # reduciendo el muestreo, se evita mensajes dobles!

        if muestra > 17 :
            muestra = contador = 0

        # if 510 < frecuenciaestimada < 520 :

        if 3100 < frecuenciaestimada < 3300:
            # parece que llega un dato, acumular hasta 3
            contador = contador + 1
        if contador > 2 :
            # confirmado que hay dato!
            if 310 < frecuenciaestimada < 370 :
                print("INICIO DE MENSAJE ---------------------------", frecuenciaestimada)
                mensajein = 1
                mensaje = ""
            if 210 < frecuenciaestimada < 270 :
                print ("FINAL DE MENSAJE ---------------------------", frecuenciaestimada)
                print ("CODED:", mensaje)
                msgcoded = mensaje.split(sep="/")[0]
                decodifica = bytes.fromhex(msgcoded).decode('utf-8')
                print("------- DECODE:::::: ", decodifica)
                mensaje = ""
            if 2450 < frecuenciaestimada < 2550 :
                print("SEPARADOR ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "/"
            if 430 < frecuenciaestimada < 470 :
                print ("LETRA A ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "a"
            if 530 < frecuenciaestimada < 570 :
                print ("LETRA B ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "b"
            if 630 < frecuenciaestimada < 670 :
                print ("LETRA C ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "c"
            if 730 < frecuenciaestimada < 770 :
                print ("LETRA D ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "d"
            if 830 < frecuenciaestimada < 890 :
                print ("LETRA E ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "e"
            if 930 < frecuenciaestimada < 980 :
                print ("LETRA F ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "f"
            if 1030 < frecuenciaestimada < 1080 :
                print ("NUMERO 1 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "1"
            if 1150 < frecuenciaestimada < 1190 :
                print ("NUMERO 2 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "2"
            if 1250 < frecuenciaestimada < 1300 :
                print ("NUMERO 3 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "3"
            if 1390 < frecuenciaestimada < 1440 :
                print ("NUMERO 4 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "4"
            if 1500 < frecuenciaestimada < 1580 :
                print ("NUMERO 5 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "5"
            if 1600 < frecuenciaestimada < 1680 :
                print ("NUMERO 6 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "6"
            if 1700 < frecuenciaestimada < 1780 :
                print ("NUMERO 7 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "7"
            if 1800 < frecuenciaestimada < 1880 :
                print ("NUMERO 8 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "8"
            if 1900 < frecuenciaestimada < 1980 :
                print ("NUMERO 9 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "9"
            if 2000 < frecuenciaestimada < 2080 :
                print ("NUMERO 0 ---------------------------", frecuenciaestimada)
                contador = muestra = 0
                if mensajein == 1 :
                    mensaje = mensaje + "0"
        past.pop(0)
        past.append(frecuenciaestimada)

    stream.stop_stream()
    stream.close()
    p.terminate()

while True :
    print(mensaje)
    listen()
