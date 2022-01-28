import skimage
from skimage.viewer import ImageViewer

img = skimage.io.imread(fname="../images/geofront-abstract.png")
test = ImageViewer(img)

blur = skimage.filters.gaussian(
    img, sigma=(10, 10), truncate=3.5, multichannel=True)

viewer = ImageViewer(blurred)
viewer.show()

skimage.io.imsave(fname="../images/geofront-blurred.png")