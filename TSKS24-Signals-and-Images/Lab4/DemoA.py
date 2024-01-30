from preamble import *

im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
im1gray = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2GRAY)
im2_bgr = cv2.imread('image2.png')
im2 = cv2.cvtColor(im2_bgr, cv2.COLOR_BGR2RGB)
im2gray = cv2.cvtColor(im2_bgr, cv2.COLOR_BGR2GRAY)


y, cb, cr = jl.rgb2ycbcr(im1)

mse = np.mean((im1gray-y)**2)
psnr = 10*np.log10(255**2/mse)


plt.figure(2), plt.imshow(y, 'gray', clim=(0,255))
plt.figure(3), plt.imshow(cb, 'gray')
plt.figure(4), plt.imshow(cr, 'gray')
plt.show()
