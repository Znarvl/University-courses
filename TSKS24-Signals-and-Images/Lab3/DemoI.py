from preamble import *

pattern = np.load('pattern.npy')

plt.subplot(231)
plt.imshow(pattern,'gray',clim=(-1,1))
plt.title('original pattern')

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
aver = signal.convolve2d(b2,b2.T)

lp_pattern = signal.convolve2d(pattern,aver,'same')
#repeating the convulation
lp_pattern2 = signal.convolve2d(lp_pattern,aver,'same')
lp_pattern3 = signal.convolve2d(lp_pattern2,aver,'same')
lp_pattern4 = signal.convolve2d(lp_pattern3,aver,'same')
lp_pattern5 = signal.convolve2d(lp_pattern4,aver,'same')
lp_pattern6 = signal.convolve2d(lp_pattern5,aver,'same')
lp_pattern7 = signal.convolve2d(lp_pattern6,aver,'same')
lp_pattern8 = signal.convolve2d(lp_pattern7,aver,'same')


plt.subplot(232)
plt.imshow(pattern[::2,::2],'gray',clim=(-1,1))
plt.title('downsampled pattern')

plt.subplot(233)
plt.imshow(lp_pattern,'gray',clim=(-1,1))
plt.title('lp pattern')


plt.subplot(234)
plt.imshow(lp_pattern[::2,::2],'gray',clim=(-1,1))
plt.title('sampled lpx1 pattern')

plt.subplot(235)
plt.imshow(lp_pattern4[::2,::2],'gray',clim=(-1,1))
plt.title('sampled lpx4 pattern')

plt.subplot(236)
plt.imshow(lp_pattern8[::2,::2],'gray',clim=(-1,1))
plt.title('sampled lpx8 pattern')

plt.show()
