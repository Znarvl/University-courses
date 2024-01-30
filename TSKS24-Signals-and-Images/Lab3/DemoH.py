from preamble import *

Im = np.double(imageio.imread('circle.tif'))
pirat = np.load('pirat.npy')
Im = pirat

plt.subplot(221)
plt.imshow(Im, 'gray', clim=(0,255))
plt.title('original image')
plt.colorbar()

lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
Imlap = signal.convolve2d(Im,lap,'same')

pirat_hp = -Imlap
sharp_pirat = Im + pirat_hp
sharp_pirat2 = Im + pirat_hp*2
sharp_pirat4 = Im + pirat_hp*4
neg_pirat = Im - pirat_hp

plt.subplot(222)
plt.imshow(sharp_pirat, 'gray', clim=(0,250))
plt.title('sharper image')
plt.colorbar()

plt.subplot(223)
plt.imshow(neg_pirat, 'gray', clim=(0,250))
plt.title('neg image')
plt.colorbar()

plt.subplot(224)
plt.imshow(sharp_pirat4, 'gray', clim=(-0,250))
plt.title('sharper image x4')
plt.colorbar()


plt.show()
