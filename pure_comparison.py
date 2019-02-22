import numpy as np

import soundfile as sf

from scipy.io import wavfile
import matplotlib.pyplot as plt
data_t, fs_t = sf.read('Hello_I_hear_you.wav') # load the data
data_r, fs_r = sf.read('microphone-results.wav')
        #checks if signal is stereo
if data_t.ndim >= 2:
    data_t = data_t.T[0]
if data_r.ndim >= 2:
    data_r = data_r.T[0]

corr_vec = np.correlate(data_t, data_r, 'full')
        #normalized_vec = corr_vec/max(abs(corr_vec[:]))
        #max_lag = np.argmax(normalized_vec)
av_value = np.mean(corr_vec)
max_value = corr_vec[np.argmax(abs(corr_vec))]
normalized_vec = corr_vec/max_value
# calculate how many percent of the max value makes the mean value
# this is used to define if there exists a peak in the correlation spectrum
percentage_value = (av_value*100)/max_value # output in percent
if percentage_value  <= 0.00011:
    print('Signals are the same!')
else:
    print('Signals have diverged!')


max_lag= np.argmax(abs(corr_vec))
t_dif = max_lag/fs_t
'''
plt.figure()
plt.plot(normalized_vec)
plt.xlabel('Time Lags')
plt.ylabel('Correlation Factor')
plt.title('Correlation Vector',fontsize=18)
plt.show()
'''

'''
plt.figure(1)
plt.plot(data_r)
plt.xlabel('Time(s)')
plt.ylabel('Waveform')
plt.title('Received signal from the loudspeaker',fontsize=18)
#plt.ylim((-0.3,0.3))
plt.show()
'''
plt.subplot(2,1,1)
#plt.legend((p1[0], p2[0]), ('Input Signal to the target', 'Received signal from the loudspeaker'),loc = 'upper right')
p1 = plt.plot(data_t)
plt.xlabel('Time(s)')
plt.ylabel('Waveform')
plt.title('Input signal to the target',fontsize=18)
plt.subplot(2,1,2)
p2 = plt.plot(data_r,'y')
plt.xlabel('Time(s)')
plt.ylabel('Waveform')
plt.title('Received signal from the loudspeaker',fontsize=18)
plt.show()
'''
plt.figure(2)
plt.plot(data_t)
plt.xlabel('Time(s)')
plt.ylabel('Waveform')
plt.title('Input signal to the target',fontsize=18)
#plt.ylim((-0.3,0.3))
plt.show()
'''
