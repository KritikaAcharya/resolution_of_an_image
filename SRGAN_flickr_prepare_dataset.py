
import os
import cv2

# Specify the input directory
input_dir = "mirflickr"

# Specify the output directories
hr_output_dir = "hr_images"
lr_output_dir = "lr_images"

# Create output directories if they don't exist
os.makedirs(hr_output_dir, exist_ok=True)
os.makedirs(lr_output_dir, exist_ok=True)

# Loop through images in the input directory
for img in os.listdir(input_dir):
    # Read the image
    img_path = os.path.join(input_dir, img)
    img_array = cv2.imread(img_path)
    
    # Resize the image for high resolution
    hr_img_array = cv2.resize(img_array, (128, 128))

    # Resize the image for low resolution
    lr_img_array = cv2.resize(img_array, (32, 32))

    # Save the high-resolution image
    hr_img_path = os.path.join(hr_output_dir, img)
    cv2.imwrite(hr_img_path, hr_img_array)

    # Save the low-resolution image
    lr_img_path = os.path.join(lr_output_dir, img)
    cv2.imwrite(lr_img_path, lr_img_array)