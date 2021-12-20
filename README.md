# denoising-of-signals-using-wavelet-transform-

In this project I have tried to implement wavelet transform to denoise various 1-D signals like mono channel audio signal (wav file), my work flow was :

(a) Take a noisy signal apply discrete wavelet transform to it. 
(b) Now set a threshold level for decomposition of wavelet transform. 
(c) Lastly, apply Inverse discrete wavelet transform to retrieve filtered/denoised signal.

Also, significant results were found when wavelet transform was applied to 2-D Signals like images
In this I used two methods i.e Bayes Shrink and Visu Shrink to denoise image.
And for analysis purpose, included calculated peak-signal-to-noise-ratio or PSNR for aforesaid methods and for noisy & original image.


Tech used - Python 3.8, Spyder and Anaconda

NOTE: to run audio denoising in spyder.io, one must install sound device package to get to listen to various outputs using below commands in cmd-

      conda install -c conda-forge python-sounddevice
      
      Later, after installing above package you can listen to noisy and denoised audio using these commands in console:
      
      import sounddevice as sd
      sd.play(x_noisy,Fs)
      sd.play(x_denoise,Fs)

Congrats!!! you have successfully denoised various types of signals using wavelet transform.

Hope, you liked my work. 
For any query, u can write me at: neoarya2012@gmail.com
