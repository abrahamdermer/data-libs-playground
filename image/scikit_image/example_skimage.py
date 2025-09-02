from skimage import data, filters, io
img = data.camera()  # small built-in grayscale image
edges = filters.sobel(img)
io.imsave("image/skimage_edges.png", (edges*255).astype("uint8"))
print("Saved image/skimage_edges.png")
