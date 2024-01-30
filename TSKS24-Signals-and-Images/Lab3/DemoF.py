from preamble import *

Im = np.double(imageio.imread('circle.tif'))

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
d = np.array([1.0,-1.0])
cd = np.convolve(b,d).reshape(1,3)
sobelx = signal.convolve2d(cd,b2.T)
sobely = sobelx.T

Imsobelx = signal.convolve2d(Im,sobelx,'same')
Imsobely = signal.convolve2d(Im,sobely,'same')
Immagnituden = np.hypot(Imsobelx,Imsobely)

Imcd = signal.convolve2d(Im,cd,'same')
Immagcd = np.hypot(Imcd, Imcd.T)

plt.subplot(221)
plt.imshow(Immagnituden, 'gray', clim=(0,160))
plt.title('magnitude sobel')
plt.colorbar()

plt.subplot(223)
plt.imshow(Immagnituden, 'gray', clim=(90,160))
plt.title('magnitude sobel')
plt.colorbar()

plt.subplot(222)
plt.imshow(Immagcd, 'gray', clim=(0,160))
plt.title('magnitude cd')
plt.colorbar()

plt.subplot(224)
plt.imshow(Immagcd, 'gray', clim=(90,160))
plt.title('magnitude cd')
plt.colorbar()

plt.show()
