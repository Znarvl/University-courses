from preamble import *

Im = np.double(imageio.imread('baboon.tif'))
plt.subplot(221)
plt.imshow(Im, 'gray', clim=(0,255))
plt.title('original image')
plt.colorbar()

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
d = np.array([1.0,-1.0])
cd = np.convolve(b,d).reshape(1,3)
sobelx = signal.convolve2d(cd,b2.T)
sobely = sobelx.T

Imsobelx = signal.convolve2d(Im,sobelx,'same')
Imsobely = signal.convolve2d(Im,sobely,'same')
Immagnituden = np.hypot(Imsobelx,Imsobely)

plt.subplot(222)
plt.imshow(Immagnituden, 'gray', clim=(0,130))
plt.title('magnitude image')
plt.colorbar()

plt.subplot(223)
plt.imshow(Imsobelx, 'gray', clim=(-128,127))
plt.title('sobelx image')
plt.colorbar()

plt.subplot(224)
plt.imshow(Imsobely, 'gray', clim=(-128,127))
plt.title('sobely image')
plt.colorbar()

plt.show()
