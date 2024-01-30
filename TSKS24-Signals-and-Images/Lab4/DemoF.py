from preamble import *
im1_bgr = cv2.imread('image1.png')
im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
y, cb, cr = jl.rgb2ycbcr(im1)

Yb = jl.bdct(y, (8, 8))
'''
Q1 = 25
Ybq = jl.bquant(Yb, Q1)
Ybr = jl.brec(Ybq, Q1)
yr = jl.ibdct(Ybr, (8, 8), (512, 768))
plt.figure(3), plt.imshow(yr, 'gray', clim=(0, 255))
'''
Q2 = 2.8
Ybq = jl.bquant(Yb, jl.jpgqmtx()*Q2)
Ybr = jl.brec(Ybq, jl.jpgqmtx()*Q2)
yr = jl.ibdct(Ybr, (8, 8), (512, 768))
plt.figure(4), plt.imshow(yr, 'gray', clim=(0, 255))

Qm = jl.jpgqmtx()
Qm.reshape(8, 8)

'''
JPEGMEAN = np.mean(Qm)

print(JPEGMEAN*Q2)

mse = np.mean((y-yr)**2)
psnr = 10*np.log10(255**2/mse)
print(psnr)



plt.show()
'''
dct_block = np.arange(64)
Z = jl.zigzag_matrix()
zigzagged_block = Z@dct_block #@ means matrix multiplication in numpy
zigzag_indices = jl.zigzag_indices()
'''
plt.plot(np.mean(np.abs(Ybq), axis=1)[1:])
plt.plot((Z@np.mean(np.abs(Ybq), axis=1))[1:])
plt.legend(["original", "zig-zag"])
plt.show()
'''
