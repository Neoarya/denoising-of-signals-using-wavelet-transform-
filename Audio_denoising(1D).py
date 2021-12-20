from scipy.io import wavfile
import numpy as np
from skimage.restoration import denoise_wavelet
import matplotlib.pyplot as plt

from pydub import AudioSegment
sound = AudioSegment.from_wav("conv.wav")
sound = sound.set_channels(1)
sound.export("ex1.wav", format="wav")

Fs, x = wavfile.read('ex1.wav') #Reading Audio Wave File
x = x/max(x) #Normalizing Amplitude

sigma = 0.04 #Noise Variance
x_noisy = x + sigma * np.random.randn(x.size) #Adding Noise to Signal

#Wavelet Denoising 
x_denoise = denoise_wavelet(x_noisy, method='BayesShrink', mode='soft', wavelet_levels=3,
                           wavelet='sym8', rescale_sigma='True')

plt.figure(figsize=(20, 10),dpi=100)
plt.plot(x_noisy)
plt.plot(x_denoise)


