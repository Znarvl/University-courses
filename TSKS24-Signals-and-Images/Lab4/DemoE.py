from preamble import *
im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
y, cb, cr = jl.rgb2ycbcr(im1)

'''
question 13
plt.figure(2), plt.imshow(y, 'gray', clim=(0, 255))
Yb = jl.bdct(y, (8, 8))
ulim = np.max(np.abs(Yb))/10
plt.figure(3), plt.imshow(np.abs(Yb), 'gray', clim=(0, ulim))

yn = jl.ibdct(Yb, (8, 8), (512,768))
plt.figure(4), plt.imshow(yn, 'gray', clim=(0, 255)), plt.show()
result = np.max(np.abs(y-yn))
'''
Yb = jl.bdct(y, (8, 8))
Ybq = np.zeros(Yb.shape)
Ybq[(0, 1, 2, 8, 9, 10, 16, 17, 18), :] = np.round(Yb[(0, 1, 2, 8, 9, 10, 16, 17, 18), :])
yq2 = jl.ibdct(Ybq, (8, 8), (512, 768))
plt.figure(3), plt.imshow(yq2, 'gray', clim=(0, 255)), plt.show()

mse = np.mean((y-yq2)**2)
psnr = 10*np.log10(255**2/mse)
print(psnr)

#maxv = np.max(Ybq)
#minv = np.min(Ybq)