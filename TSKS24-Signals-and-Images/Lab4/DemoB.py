from preamble import *

im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
y,cb,cr = jl.rgb2ycbcr(im1)
ycbcr = jl.rgb2ycbcr(im1)
im2_bgr = cv2.imread('image2.png')
im2 = cv2.cvtColor(im2_bgr, cv2.COLOR_BGR2RGB)
im3_bgr = cv2.imread('image3.png')
im3 = cv2.cvtColor(im3_bgr, cv2.COLOR_BGR2RGB)

im1r = im1[:,:,0]
im1g = im1[:,:,1]



plt.figure(2), plt.imshow(y, 'gray', clim=(0, 255))
y2 = 4*np.floor_divide(y, 4)
plt.figure(3), plt.imshow(y2, 'gray', clim=(0, 255))

mse = np.mean((y-y2)**2)
psnr = 10*np.log10(255**2/mse)

print(psnr)
plt.show()
