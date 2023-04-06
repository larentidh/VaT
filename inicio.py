# Importar la biblioteca SpeechRecognition y crear un objeto "Recognizer":
import speech_recognition as sr

r = sr.Recognizer()

# Abrir el archivo de audio utilizando la biblioteca "WavFile" de la biblioteca "scipy":

from scipy.io.wavfile import read

# Reemplaza "ruta_al_archivo" con la ubicación del archivo de audio que deseas transcribir
archivo_audio = read('p4.wav')

# Extraer la frecuencia de muestreo y los datos de audio del archivo
frecuencia_muestreo = archivo_audio[0]
datos_audio = archivo_audio[1]

# Transcribir el audio utilizando el objeto "Recognizer":

with sr.AudioFile('p4.wav') as source:
    audio = r.record(source)

# Utilizar el objeto "Recognizer" para transcribir el audio a texto
texto = r.recognize_google(audio, language='es-AR')

# Imprimir el texto transrito:

print(texto)

