import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
from convert import convert_wav
import matplotlib.pyplot as plt


# generate mfcc file for each 30 second wav sample
def create_mfcc(file):
    sample_rate, X = scipy.io.wavfile.read(file)
    m, mspec, spec = mfcc(X, fs=sample_rate)
    all = m.tolist()
    return all

def plot_spec(file, song_title):
    #load wav file
    sample_rate, X = scipy.io.wavfile.read(file)
    #create specgram plot
    plt.specgram(X, Fs=sample_rate, xextent=(0, 30))
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (kHz)')
    g = get_genre(file)
    plt.title(g + " Specgram \n" + "Song: " + song_title)
    plt.show()

def get_genre(file):
    genres = ["Country", "Electronic", "Hip Hop", "Rock", "Jazz"]
    for g in genres:
        if g in file:
            return g

plot_spec("/Users/sina/Documents/Dataset/Jazz/wav/360.wav", "Miles Davis - Round Midnight")
plot_spec("/Users/sina/Desktop/Hip Hop/282.wav",  "J Dilla - E=MC2")
plot_spec("/Users/sina/Documents/Dataset/Electronic/wav/176.wav", "Disclosure - Jaded")
plot_spec("/Users/sina/Documents/Dataset/Rock/wav/540.wav", "Mac Demarco - Salad Days")
plot_spec("/Users/sina/Documents/Dataset/Country/wav/058.wav", "Johnny Cash- I Walk the Line")




