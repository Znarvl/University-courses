from preamble import *

im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
y,cb,cr = jl.rgb2ycbcr(im1)

Y = cv2.dct(y)
plt.figure(3), plt.imshow(np.log(np.abs(Y)+1), 'gray')
plt.show()

Yq = np.zeros((512,768))
Yq[0:128,0:196] = np.round(Y[0:128,0:196])
plt.figure(4), plt.imshow(np.log(np.abs(Yq)+1),'gray')
yq = cv2.idct(Yq)
plt.figure(5),plt.imshow(yq,'gray',clim=(0,255))

mse = np.mean((y-yq)**2)
psnr = 10*np.log10(255**2/mse)
print(psnr)
plt.show()