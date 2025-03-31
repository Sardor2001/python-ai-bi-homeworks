from PIL import Image
import numpy as np


# Function to flip the image horizontally and vertically
def flip_image(image_array):
    # Flip horizontally (left-to-right)
    flipped_horizontal = np.fliplr(image_array)
    # Flip vertically (up-to-down)
    flipped_vertical = np.flipud(flipped_horizontal)
    return flipped_vertical


# Function to add random noise to the image
def add_noise(image_array, noise_level=30):
    # Generate random noise in the range [-noise_level, noise_level]
    noise = np.random.randint(-noise_level, noise_level, image_array.shape, dtype=np.int16)
    # Add noise to the image and clip values to [0, 255]
    noisy_image = np.clip(image_array.astype(np.int16) + noise, 0, 255)
    return noisy_image.astype(np.uint8)


# Function to brighten a specific channel (e.g., red, green, blue)
def brighten_channels(image_array, channel_index, value=40):
    # Increase the brightness of the specified channel
    image_array[:, :, channel_index] = np.clip(image_array[:, :, channel_index] + value, 0, 255)
    return image_array


# Function to apply a rectangular mask to the image
def apply_mask(image_array, x, y, width, height):
    # Set the pixel values in the rectangular region to black (0, 0, 0)
    image_array[y:y + height, x:x + width] = [0, 0, 0]
    return image_array


# Load the image using PIL
image_path = "birds.png"
image = Image.open(image_path)
image_array = np.array(image)  # Convert image to NumPy array

# 1. Flip the image
flipped_image_array = flip_image(image_array)
flipped_image = Image.fromarray(flipped_image_array)
flipped_image.save("flipped_birds.png")

# 2. Add random noise
noisy_image_array = add_noise(image_array, noise_level=50)
noisy_image = Image.fromarray(noisy_image_array)
noisy_image.save("noisy_birds.png")

# 3. Brighten the red channel
brightened_image_array = brighten_channels(image_array, channel_index=0, value=40)
brightened_image = Image.fromarray(brightened_image_array)
brightened_image.save("brightened_birds.png")

# 4. Apply a mask to the center of the image
height, width, _ = image_array.shape
mask_width, mask_height = 100, 100
x = (width - mask_width) // 2  # Center x-coordinate
y = (height - mask_height) // 2  # Center y-coordinate
masked_image_array = apply_mask(image_array, x, y, mask_width, mask_height)
masked_image = Image.fromarray(masked_image_array)
masked_image.save("masked_birds.png")
