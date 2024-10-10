import numpy as np
import matplotlib.pyplot as plt


#File-location "Change-accordingly"
spectrum = np.loadtxt('/home/athul/Py3/tau_LOS_A.txt')


#Read-arrays
velocity = spectrum[:, 1]
opticaldepth = spectrum[:, 2]


flux = np.exp(-opticaldepth)
x_array = np.arange(0, len(flux), 1) 


for resolution in [2000,50000]:

    mu = len(x_array)/2
    light_c = 3 * (10**5)
    FWHM = light_c/resolution
    sigma = FWHM/(2*np.sqrt(2*np.log(2)))
    gauss_arr = []

    #Gaussian

    def gaussian(x, mu, sigma):

        gus = (1/(sigma*(np.sqrt(2*np.pi)))) * np.exp(-0.5*(((x-mu)/sigma)**2))

        return gus

    #Convolution

    def convolution(input, sigma):

        fft_input = np.fft.fft(input)

        for x in x_array:

            gus = gaussian (x, mu, sigma)
            gauss_arr.append(gus) 

        fft_gauss = (np.fft.fft(gauss_arr))

        convolved_fft = fft_input * fft_gauss

        convolved = np.fft.fftshift(np.fft.ifft(convolved_fft))
    
        return convolved

    smoothed_flux = convolution(flux, sigma)


#Plot-section
    if resolution == 2000:

        fig, (plot1, plot2, plot3) = plt.subplots(3,1, figsize = (16,10), sharex=True, sharey=True)

        plot1.plot(velocity, flux, label = "Transmitted Flux Average:"+ str(np.mean(flux)),color="red")

        plot2.plot(velocity, flux,color="red")
        plot2.plot(velocity, np.abs(smoothed_flux), label = "Smoothed Flux Average   :"+ str(np.mean(np.abs(smoothed_flux))),color="green")
        
    
    elif resolution == 50000:

        plot3.plot(velocity, flux, color="red")
        plot3.plot(velocity, np.abs(smoothed_flux), label = "Smoothed Flux Average   :"+ str(np.mean(np.abs(smoothed_flux))),color="green")
           

plot1.legend(loc = "upper right")
plot2.legend(loc = "upper right")
plot3.legend(loc = "upper right")
fig.supxlabel("Velocity Offset")
fig.supylabel("Transmitted Flux Fraction")
fig.suptitle('Lyman-alpha Forest Spectrum')
plt.show()