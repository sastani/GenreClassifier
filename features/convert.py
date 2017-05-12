from pydub.audio_segment import AudioSegment
import os

#convert to 30 second mono sample
def convert_wav(file, counter):
    filename, ext = os.path.splitext(file)
    wav_dir = os.path.dirname(file) + "/wav"
    if not os.path.exists(wav_dir):
        os.mkdir(wav_dir)
    ext = ext[1:]
    song = AudioSegment.from_file(file, ext)
    msecs = song.duration_seconds * 1000
    halfpoint = msecs/2
    thir_sec = song[halfpoint:(halfpoint+30000)]
    thir_sec = thir_sec.set_channels(1)
    new_filename = wav_dir + "/" + str(counter) + ".wav"
    thir_sec.export(new_filename, format="wav")
    return new_filename