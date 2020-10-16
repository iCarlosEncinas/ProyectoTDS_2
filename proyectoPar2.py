import sys 
sys.path.insert(1,'dsp-modulo')

from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from thinkdsp import read_wave
import numpy

principal = Tk()
principal.title("Analisis audio")


strDireccionArchivo = StringVar()
strDireccionArchivo.set("Direccion del archivo:")

strSecuencia = StringVar()
strSecuencia.set("Numero de contenido en el audio:")

def abrirArchivo():
    direccionArchivo = askopenfilename()
    strDireccionArchivo.set("Direccion del archivo: " + direccionArchivo)

    tamanoSegmento = 0
    tamanoLetras = 0
    palabra = ""
    wavePalabra = read_wave(direccionArchivo)
    primerSegmentoLetras = []
    
    primerSegmentoLetras.append(wavePalabra.segment(start=0, duration=0.5))


    frecuenciasSegmentos = [300, 400, 500, 600]
    frecuenciasNumeroLetras = [2000, 2600, 2300, 3200, 3500, 2900, 3800]
    tolerancia = 10

    for segmento in primerSegmentoLetras:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        sizeSegmento = 0
        cantidadLetras = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciasSegmentos:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    sizeSegmento = frecuenciaDTMF
            for frecuenciaDTMF in frecuenciasNumeroLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    cantidadLetras = frecuenciaDTMF

        if sizeSegmento == 300:
            tamanoSegmento = 0.3
        elif sizeSegmento == 400:
            tamanoSegmento = 0.4
        elif sizeSegmento == 500:
            tamanoSegmento = 0.5
        elif sizeSegmento == 600:
            tamanoSegmento = 0.6

        if cantidadLetras == 2000:
            tamanoLetras = 2
        elif cantidadLetras == 2600:
            tamanoLetras = 3
        elif cantidadLetras == 2300:
            tamanoLetras = 4
        elif cantidadLetras == 3200:
            tamanoLetras = 5
        elif cantidadLetras == 3500:
            tamanoLetras = 6
        elif cantidadLetras == 2900:
            tamanoLetras = 7
        elif cantidadLetras == 3800:
            tamanoLetras = 8

    
    segmentoLetras = []
    for i in range(tamanoLetras):
        segmentoLetras.append(wavePalabra.segment(start=0.5+i*tamanoSegmento, duration=tamanoSegmento))
    

    frecuenciaLetras = [2000, 5600, 9200, 2400, 6000, 9600, 2800, 6400, 10000, 3200, 6800, 10400, 3600, 7200, 10800, 4000, 7600, 11200, 4400, 8000, 11600, 4800, 8400, 12000, 5200, 8800]


    for segmento in segmentoLetras:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        letras = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    letras = frecuenciaDTMF
        
        if letras == 2000:
            palabra = palabra + "A"
        elif letras == 5600:
            palabra = palabra + "B"
        elif letras == 9200:
            palabra = palabra + "C"
        elif letras == 2400:
            palabra = palabra + "D"
        elif letras == 6000:
            palabra = palabra + "E"
        elif letras == 9600:
            palabra = palabra + "F"
        elif letras == 2800:
            palabra = palabra + "G"
        elif letras == 6400:
            palabra = palabra + "H"
        elif letras == 10000:
            palabra = palabra + "I"
        elif letras == 3200:
            palabra = palabra + "J"
        elif letras == 6800:
            palabra = palabra + "K"
        elif letras == 10400:
            palabra = palabra + "L"
        elif letras == 3600:
            palabra = palabra + "M"
        elif letras == 7200:
            palabra = palabra + "N"
        elif letras == 10800:
            palabra = palabra + "O"
        elif letras == 4000:
            palabra = palabra + "P"
        elif letras == 7600:
            palabra = palabra + "Q"
        elif letras == 11200:
            palabra = palabra + "R"
        elif letras == 4400:
            palabra = palabra + "S"
        elif letras == 8000:
            palabra = palabra + "T"
        elif letras == 11600:
            palabra = palabra + "U"
        elif letras == 4800:
            palabra = palabra + "V"
        elif letras == 8400:
            palabra = palabra + "W"
        elif letras == 12000:
            palabra = palabra + "X"
        elif letras == 5200:
            palabra = palabra + "Y"
        elif letras == 8800:
            palabra = palabra + "W"

    strSecuencia.set("Numero de contenido en el audio: " + palabra)

    figure = Figure(figsize = (5,3), dpi = 100)
    figure.add_subplot(111).plot(wavePalabra.ts, wavePalabra.ys)
    canvas = FigureCanvasTkAgg(figure, master = principal)
    canvas.draw()
    canvas.get_tk_widget().pack()




btnAbrir = Button(principal, text = "Abriri archivo wav", command = abrirArchivo)
btnAbrir.pack()

lblArchivo = Label(principal, textvariable = strDireccionArchivo)
lblArchivo.pack()

lblSecuenciaNumeros = Label(principal, textvariable = strSecuencia)
lblSecuenciaNumeros.pack()

mainloop()