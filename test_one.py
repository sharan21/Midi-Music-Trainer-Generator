from mido import MidiFile
import numpy as np


mid = MidiFile('./midi//fur_elise.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for message in track:
        print(message)