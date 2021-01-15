from math import sin, pi
from datetime import datetime


class SignalGenerator:

    def __init__(self, freqs, ampls):
        self.frequencies = freqs
        self.amplitudes = ampls
        self.start_time = datetime.now()

    def get_signal(self):
        total_output = 0
        t = (datetime.now() - self.start_time).total_seconds()

        for f, a in zip(self.frequencies, self.amplitudes):
            output = a * sin(2 * pi * f * t)
            total_output += output

        return total_output
