from preamble import *

Im = np.load('pirat2.npy')
IM = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(Im)))

IMre = np.real(IM)
IMabs = np.abs(IM)
maxv = -0.1*np.min(IMre)
medel = np.mean(IMabs)
IMang = np.angle(IM)

IMang[medel*10>IMabs] =0

plt.subplot(221), plt.imshow(np.abs(IM),'gray', clim =(0,maxv)), plt.colorbar()
plt.subplot(222), plt.imshow(IMang,'gray'), plt.colorbar()
plt.subplot(223), plt.imshow(np.real(IM),'gray', clim =(-maxv,maxv)), plt.colorbar()
plt.subplot(224), plt.imshow(np.imag(IM),'gray', clim =(-maxv,maxv)), plt.colorbar()

plt.show()
