import os
import librosa
from utils import extract_vocal
import warnings
import soundfile as sf
warnings.filterwarnings('ignore')
PATH = '/home/huudu/y4/dp/spotify-to-mp3-python/Mãi Yêu Đen/'
all_songs = os.listdir(PATH)
sr = 44100

# Generate mixtures, others and vocals files
for i, fname in enumerate(all_songs):
    if fname.split('.')[-1] != 'wav':
        continue
    master, vocal, other = extract_vocal(
        os.path.join(PATH, fname),  sample_rate=sr)
    sf.write('data/mixtures/{}.wav'.format(i), master, sr)
    #sf.write('data/vocals/{}.wav'.format(i), vocal, sr)
# sf.write('data/others/{}.wav'.format(i), other, sr)
