from signal_generator import SignalGenerator
from time import sleep, time
import numpy as np
from scipy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt


sampling_rate = 400
duration = 5

signalGen = SignalGenerator([1.0, 0.5], [1.0, 1.0])


#while True:
if True:
    sampling_start = time()
    samples = []
    last_sample = time()
    while time() - sampling_start < duration:
        while time() - last_sample < 1/sampling_rate:
            pass
        samples.append(signalGen.get_signal())
        last_sample = time()
    sampling_end = time()

    samples = np.array(samples)
    samples = samples / max(samples)

    N = len(samples)
    effective_duration = sampling_end - sampling_start
    effective_rate = N / effective_duration

    x = np.linspace(0, effective_duration, N, endpoint=False)

    plt.plot(x, samples)
    plt.show()

    yf = rfft(samples)
    xf = rfftfreq(N, 1 / effective_rate)

    plt.plot(xf, np.abs(yf))
    plt.show()


