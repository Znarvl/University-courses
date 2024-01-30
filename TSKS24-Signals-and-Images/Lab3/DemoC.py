from preamble import *

Im = np.double(imageio.imread('baboon.tif'))
plt.subplot(121)
plt.imshow(Im, 'gray', clim=(0,255))
plt.title('original image')
plt.colorbar()

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
aver = signal.convolve2d(b2,b2.T)
Imaver = signal.convolve2d(Im,aver,'same')
#repeating the convulation twice
Imaver = signal.convolve2d(Imaver,aver,'same')
Imaver = signal.convolve2d(Imaver,aver,'same')

plt.subplot(122)
plt.imshow(Imaver, 'gray', clim=(0,255))
plt.title('aver image')
plt.colorbar()

plt.show()