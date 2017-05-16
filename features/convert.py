from pydub.audio_segment import AudioSegment
from pydub.utils import make_chunks
from functools import reduce
import os

#convert mp3 to 30 second mono wav sample
def convert_wav(file, counter):
    filename, ext = os.path.splitext(file)
    wav_dir = os.path.dirname(file) + "/wav"
    if not os.path.exists(wav_dir):
        os.mkdir(wav_dir)
    ext = ext[1:]
    song = AudioSegment.from_file(file, ext)
    msecs = song.duration_seconds * 1000
    halfpoint = msecs/2
    thir_sec = song[halfpoint:(halfpoint+15000)]
    sample_rate = thir_sec.frame_rate
    #standard decibel range
    normal_db = [-32.0, -18.0]
    #normalize sample before stripping a channel to avoid clipping
    thir_sec = normalize(thir_sec, sample_rate, normal_db)
    #convert to mono
    thir_sec = thir_sec.set_channels(1)
    new_filename = wav_dir + "/" + str(counter) + ".wav"
    thir_sec.export(new_filename, format="wav")
    return new_filename


#change the amplitude level/loudness of audio segment to avoid clipping
#loudness is measured in decibels relative to full scale (dbfs)
def change_loudness(sample, target_dbfs):
    change = target_dbfs - sample.dBFS
    return sample.apply_gain(change)

#normalize sample using dbfs range
def normalize(sample, sample_rate, target_dbfs):
    def max_min_volume(min, max):
        for chunk in make_chunks(sample, sample_rate):
            if chunk.dBFS < min:
                yield change_loudness(chunk, min)
            elif chunk.dBFS > max:
                yield change_loudness(chunk, max)
            else:
                yield chunk

    return reduce(lambda x, y: x + y, max_min_volume(target_dbfs[0], target_dbfs[1]))