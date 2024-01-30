from preamble import *
def on_press(event):
    print(Im[round(event.ydata), round(event.xdata)])

gbgraycmap = plt.get_cmap('gray', 256)
gbgray_vals = gbgraycmap(np.arange(256))

gbgray_vals[200:] = [0, 0, 1, 1]
gbgray_vals[:51] = [0, 1, 0, 1]
plt.register_cmap('gbgray',gbgraycmap.from_list('gbgray', gbgray_vals))
print(gbgray_vals)

Im = np.double(imageio.imread('baboon.tif'))
plt.subplot(121)
plt.imshow(Im, 'gbgray', clim=(0,255)) #change to 'jet' for question 5
plt.title('Original image')
plt.colorbar()

plt.show()