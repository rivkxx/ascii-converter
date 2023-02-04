import numpy as np
import cv2

# Load image and convert to grayscale
image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Normalize the pixel values to be between 0 and 255
gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

# Define the ASCII characters to be used
ascii_characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]

# Create an empty list to store the ASCII representation of the image
ascii_image = []

# Loop through the rows and columns of the grayscale image
for i in range(gray.shape[0]):
    row = []
    for j in range(gray.shape[1]):
        # Get the grayscale value of the current pixel
        intensity = gray[i, j]
        
        # Map the grayscale value to an ASCII character
        index = int(intensity / 25.5)
        ascii_char = ascii_characters[index]
        
        # Add the ASCII character to the current row
        row.append(ascii_char)
        
    # Add the row to the ASCII image
    ascii_image.append(row)

# Print the ASCII image
for row in ascii_image:
    print("".join(row))
