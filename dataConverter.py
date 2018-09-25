# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:56:06 2018

@author: kmyko
"""



class AudioListener:
    def __init__(self, CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS):
        self.CHUNK = CHUNK
        self. FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.RECORD_SECONDS = RECORD_SECONDS
        
    def convert(self):
        # initialise a Pyaudio object
        P = pyaudio.PyAudio()
        
        stream = P.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK) 
        stream.start_stream()
        data = stream.read(self.CHUNK) # convert stream to readable integer
        
        return data

    def toAmplitude(self):
            data = self.convert()
            # print(np.linalg.norm(np.frombuffer(data, np.int16), 2))
            return np.linalg.norm(np.frombuffer(data, np.int16), 2)
    
    def check(self):
        while True:
            i = self.toAmplitude()
            if i >= np.float64(100000):
                print(i)
                winsound.Beep(800, 100)
            # time.sleep(1)

def main():
    start = AudioListener(1024, pyaudio.paInt16, 1, 44100, 5)
    start.check()

if __name__ == "__main__":
    import pyaudio  # pacman -S portaudio && pip install pyaudio
    import numpy as np
    import winsound
    # from sound import sample
    import time

    main()
