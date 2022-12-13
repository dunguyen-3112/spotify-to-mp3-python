import stempeg
import numpy as np


def extract_vocal(fname, sample_rate=16000):
    print(fname)
    stems, sr = stempeg.read_stems(
        fname, start=60, duration=30, sample_rate=sample_rate)
    print(stems)
    stems = stems.astype(np.float32)

    master = stems[:, 0]
    vocal = stems[:, 1]
    other = stems[2, :]
    print(master[0:10])
    print(vocal[0:10])
    return master, vocal, other
