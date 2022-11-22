import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd



𝑡 = np. linspace(0 , 3 , 12*1024)
# Hash tagged Frequencies are an extra Song 😉, Remove hashtags from these frequencies and add hashtags to the other two to play it.)
#F = [185,277,370,0,146.83,220,392.63,0]
#f = [880,831,880,831,880,659.23,880,587.33]
F = [174.61,130.81,174.61,0,146.83,220,164.63,0]
f = [440,392,440,392,440,329.63,440,293.66]
ti = [0,0.37,0.74,1.11,1.48,1.85,2.22,2.59]
Ti = [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
x=0
i=0

def u(t):
    return 1*(t>=0)

while i< len(F):
    x = x +  (np.sin(2 * np.pi * F[i] * t)+ np.sin( 2 * np.pi * f[i] *t)) * (u(t-ti[i])-u(t-ti[i]-Ti[i]))
    i=i+1



plt.plot(t,x)

sd.play(x, 3 * 1024)