import matplotlib.pyplot as plt
from skimage.restoration import (denoise_wavelet, estimate_sigma)
from skimage.util import random_noise
from skimage.metrics import peak_signal_noise_ratio
import skimage.io

img = skimage.io.imread('peppers.png') #Reading Image
img = skimage.img_as_float(img) #Converting Image as float

sigma = 0.15 #Noise Std
imgn=random_noise(img, var=sigma**2) #Adding Noise

sigma_est = estimate_sigma(imgn, multichannel=True, average_sigmas=True) #Noise Estimation

#Denoising using Bayes
img_bayes = denoise_wavelet(imgn, method='BayesShrink', mode='soft', wavelet_levels=3,
                            wavelet='coif5', multichannel=True,convert2ycbcr=True, rescale_sigma=True)

#Denoising using Visushrink
img_visushrink=denoise_wavelet(imgn, method='VisuShrink', mode='soft', sigma=sigma_est/3, wavelet_levels=3,
                              wavelet='coif5', multichannel=True,convert2ycbcr=True, rescale_sigma=True)

#finding PSNR
psnr_noisy = peak_signal_noise_ratio(img,imgn)
psnr_bayes = peak_signal_noise_ratio(img, img_bayes)
psnr_visu = peak_signal_noise_ratio(img, img_visushrink)

#plotting images
plt.figure(figsize=(30,30))

plt.subplot(2,2,1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title('Original Image', fontsize=30)

plt.subplot(2,2,2)
plt.imshow(imgn, cmap=plt.cm.gray)
plt.title('Noisy Image', fontsize=30)

plt.subplot(2,2,3)
plt.imshow(img_bayes, cmap=plt.cm.gray)
plt.title('Denoised Image using Bayes', fontsize=30)

plt.subplot(2,2,4)
plt.imshow(img_visushrink, cmap=plt.cm.gray)
plt.title('Denoised Image using Visushrink', fontsize=30)

plt.show()

#printing PSNR
print('PSNR[Original vs Noisy Image]', psnr_noisy)
print('PSNR[Original vs Denoised(Visushrink)]', psnr_visu)
print('PSNR[Original vs Denoised(Bayes)]', psnr_bayes)