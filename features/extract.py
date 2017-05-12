import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc

# generate mfcc file for each 30 second wav sample
def create_mfcc(file):
    sample_rate, X = scipy.io.wavfile.read(file)
    m, mspec, spec = mfcc(X, fs=sample_rate)
    averaged_mfcc = np.mean(m[int(13 * 1 / 10):int(13 * 9 / 10)], axis=0)
    return averaged_mfcc










