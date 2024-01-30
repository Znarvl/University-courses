from preamble import *
def on_press(event):
    print(Im[round(event.ydata), round(event.xdata)])


Im = np.double(imageio.imread('baboon.tif'))
plt.subplot(121)
plt.imshow(Im, 'gray', clim=(0,255)) #change to 'ngray' for question 4
plt.title('Original image')
plt.colorbar()

plt.subplot(122)
plt.imshow(Im, 'gray', vmin=50, vmax=200)
plt.title('Contrast')
fig = plt.gcf()
fig.canvas.mpl_connect('button_press_event', on_press)
plt.colorbar()

"""
#Used for question 4

graycmap = plt.get_cmap('gray', 256)
gray_vals = graycmap(np.arange(256))
print(gray_vals)

gray_vals[200:] = [1, 0, 0, 1]
plt.register_cmap('ngray',graycmap.from_list('ngray', gray_vals))
print(gray_vals)
"""

plt.show()