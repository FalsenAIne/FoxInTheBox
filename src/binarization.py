# Imports
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
I1 = cv2.imread("../data/single_frame.png")[..., ::-1]
print(I1.shape)

# Show image
plt.imshow(I1)
plt.xticks([]), plt.yticks([])
plt.show()

# Convert image to grayscale
I_gray = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
plt.imshow(I_gray, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

# Plot histogram
hist, _ = np.histogram(I_gray, bins=256)
plt.plot(hist)
plt.show()


# Binarization
lower = 88
upper = 110
ret, img_bin = cv2.threshold(I_gray, lower, upper, cv2.THRESH_BINARY)
plt.imshow(img_bin, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()