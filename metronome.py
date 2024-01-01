import matplotlib.pyplot as plt
import scipy.special as sc
from scipy.io import wavfile
import numpy as np
import sounddevice as sd 
import warnings
import argparse


warnings.filterwarnings("ignore")
#https://python-sounddevice.readthedocs.io/en/0.4.6/installation.html
parse = argparse.ArgumentParser(description='Play metronome in CLI')
parse.add_argument('bmp',type = int, default = 60, help = 'bpm velocity') 
parse.add_argument('--vol',type = float, default = 13.0, help = 'audio volume (1-39)', required = False)
args = parse.parse_args()
amplitude = args.vol 
bpm = args.bmp 

# Loading wave file
fs, data = wavfile.read('sound.wav')
audio = np.asarray(data)
audio = amplitude * audio / np.max(audio)
duration_click = audio.size / fs
n_zeros = int((((1/(bpm / 60.0)) - duration_click)) * fs)
audio = np.append(audio, np.zeros(n_zeros))
t = np.linspace(0, (audio.size - 1) / fs, audio.size)

print('Playing metronome ' + str(args.bmp) + ' bpm')
sd.play(audio, fs, blocking = True, loop=True)
sd.stop()
#plt.plot(t, audio)
#plt.show()
