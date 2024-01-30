from preamble import *

im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
y,cb,cr = jl.rgb2ycbcr(im1)

y2 = 16*np.floor_divide(y, 16)

y3 = np.floor(ndimage.interpolation.zoom(y, 0.5, order=3))
y4 = ndimage.interpolation.zoom(y3, 2., order=3)

plt.figure(1), plt.imshow(y, 'gray', clim=(0, 255))
plt.figure(2), plt.imshow(y2, 'gray', clim=(0, 255))
plt.figure(3), plt.imshow(y4, 'gray', clim=(0, 255))

mse2 =  np.mean((y-y4)**2)
psnr2 = 10*np.log10(255**2/mse2)

print(psnr2)

plt.figure(5), plt.imshow(np.abs(y-y4), 'gray', clim=(0, 255))

plt.show()
