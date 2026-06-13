import pylab
import rtlsdr
import matplotlib.pyplot as plt

sdr = rtlsdr.RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.gain = "auto"
sdr.set_direct_sampling(0)
sdr.center_freq = 10e6

samples = sdr.read_samples(256 * 1024)
sdr.close()

# use matplotlib to estimate and plot the PSD
plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq / 1e6)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Relative power (dB)")

plt.show()
