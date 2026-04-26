import numpy as np
from PIL import Image

# image load karo
img = Image.open("input.jpg")
img_array = np.array(img)

# --------- 1. GRAYSCALE ----------
gray = np.mean(img_array, axis=2)
gray_img = gray.astype(np.uint8)

Image.fromarray(gray_img).save("gray.jpg")


# --------- 2. BRIGHTNESS INCREASE ----------
bright = img_array + 50
bright = np.clip(bright, 0, 255)

Image.fromarray(bright.astype(np.uint8)).save("bright.jpg")


# --------- 3. NEGATIVE IMAGE ----------
negative = 255 - img_array

Image.fromarray(negative.astype(np.uint8)).save("negative.jpg")

print("Done bhai 🚀")