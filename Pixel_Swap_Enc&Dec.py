import numpy as np
from PIL import Image


def generate_swap_pattern(key, length):
    np.random.seed(key)
    pattern = np.arange(length)
    np.random.shuffle(pattern)
    return pattern


def pixel_swap_encrypt(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)

    # flatten() is used to convert a multi-dimensional array (like an image) into a one-dimensional array
    flat_img = img_array.flatten()
    length = flat_img.shape[0]

    swap_pattern = generate_swap_pattern(key, length)

    encrypted_flat_img = flat_img[swap_pattern]
    encrypted_img_array = encrypted_flat_img.reshape(img_array.shape)
    encrypted_img = Image.fromarray(encrypted_img_array)

    encrypted_img_path = image_path.replace(".", "_encrypted.")
    encrypted_img.save(encrypted_img_path)

    return encrypted_img, encrypted_img_path


def pixel_swap_decrypt(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)

    flat_img = img_array.flatten()
    length = flat_img.shape[0]

    swap_pattern = generate_swap_pattern(key, length)

    decrypted_flat_img = np.zeros_like(flat_img)
    decrypted_flat_img[swap_pattern] = flat_img

    decrypted_img_array = decrypted_flat_img.reshape(img_array.shape)
    decrypted_img = Image.fromarray(decrypted_img_array)

    decrypted_img_path = image_path.replace("_encrypted.", "_decrypted.")
    decrypted_img.save(decrypted_img_path)

    return decrypted_img, decrypted_img_path


# Example usage
image_path = "download.jpg"
key = 1234  # Example key for generating the swap pattern

# Encrypt the image
encrypted_img, encrypted_img_path = pixel_swap_encrypt(image_path, key)
print(f"Encrypted image saved to: {encrypted_img_path}")

# Show the encrypted image
encrypted_img.show()

# Decrypt the image
decrypted_img, decrypted_img_path = pixel_swap_decrypt(encrypted_img_path, key)
print(f"Decrypted image saved to: {decrypted_img_path}")

# Show the decrypted image
# decrypted_img.show()
