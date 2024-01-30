from preamble import *

Im = np.double(imageio.imread('circle.tif'))
pirat = np.load('pirat.npy')
#Im = pirat

plt.subplot(221)
plt.imshow(Im, 'gray', clim=(0,255))
plt.title('original image')
plt.colorbar()

lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
Imlap = signal.convolve2d(Im,lap,'same')

plt.subplot(222)
plt.imshow(Imlap, 'gray', clim=(-100,100))
plt.title('laplace image')
plt.colorbar()

plt.show()
