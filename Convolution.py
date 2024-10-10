import numpy as np
import matplotlib.pyplot as plt


#Declarations
x_arr = np.arange(0,100,1)
mu = len(x_arr)/2
gauss = []
sigma = 5


#Input field with 100 elements
input = np.zeros(100)


#Element 50
input[49] = 1.0


#Functions
def gaussian(x, mu, sigma):

    gus = (1/(sigma*(np.sqrt(2*np.pi)))) * np.exp(-0.5*(((x-mu)/sigma)**2))

    return gus


def convolution(input, sigma):

    fft_input = np.fft.fft(input)

    for x in x_arr:

        gus = gaussian (x, mu, sigma)
        gauss.append(gus) 

    fft_gauss = (np.fft.fft(gauss))

    convolved_fft = fft_input * fft_gauss

    convolved = np.fft.fftshift(np.fft.ifft(convolved_fft))
   
    return convolved, gauss



smooth, gauss = convolution(input, sigma)

#Plot-section
plt.plot(x_arr,input, label = "Input Field, Average        :" +str(np.mean(input)))
plt.plot(x_arr, np.abs(smooth), label = "Smoothed Field, Average:" +str(np.mean(np.abs(smooth))))

plt.xlabel("Position-X")
plt.ylabel("Quantity-Y")
plt.title("Input-Field Convolution")
plt.legend(loc = "upper right")
plt.show()