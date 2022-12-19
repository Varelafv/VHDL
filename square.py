from scipy import signal

import matplotlib.pyplot as plot

import numpy as np

# Sampling rate 1000 hz / second

t = np.linspace(0, 1, 1000, endpoint=True)

# Plot the square wave signal
x=8190*signal.square(2* np.pi * 5 * t) + 8192
plot.plot(t,x)
print(min(x))
print(x)
resolution = 6
nsample     = int(360/resolution)
for k in x:
    h=k
    print('{} , '.format(h))

# Give a title for the square wave plot

plot.title('Sqaure wave - 5 Hz sampled at 1000 Hz /second')

# Give x axis label for the square wave plot

plot.xlabel('Time')

# Give y axis label for the square wave plot

plot.ylabel('Amplitude')

plot.grid(True, which='both')

# Provide x axis and line color

#plot.axhline(y=0, color='k')

# Set the max and min values for y axis

plot.ylim(-10,17000)

# Display the square wave drawn

plot.show()