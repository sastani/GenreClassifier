import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
from convert import convert_wav

# generate mfcc file for each 30 second wav sample
def create_mfcc(file):
    sample_rate, X = scipy.io.wavfile.read(file)
    m, mspec, spec = mfcc(X, fs=sample_rate)
    all = m.tolist()
    return all










