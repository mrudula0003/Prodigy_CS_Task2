import numpy as np
from PIL import Image

# function to generate a permutation (swap pattern) of indices based on a given key and length.
def generate_swap_pattern(key, length):
    np.random.seed(key)
    pattern = np.arange(length)
    # Deterministic Shuffling: Because we seeded the random number generator
    # with key earlier, this shuffle operation will produce the same result
    # every time it's run with the same key and length.
    np.random.shuffle(pattern)
    return pattern


def pixel_swap_encrypt(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)

    # flatten() is used to convert a multi-dimensional array (like an image) into a one-dimensional array
    flat_img = img_array.flatten()
    # shape is an attribute of numpy arrays that returns a tuple representing the dimensions of the array.
    length = flat_img.shape[0]

    # generating a swap pattern by assigning its parameters respectively
    swap_pattern = generate_swap_pattern(key, length)

    # Applying the swap pattern to obtained flat img (converted 1D image)
    encrypted_flat_img = flat_img[swap_pattern]
    # reshape method in numpy is used to change the shape of an array without changing its data.
    # This step converts the permuted one dimensional array back into multi dimensional array that matches the original image’s dimensions.
    encrypted_img_array = encrypted_flat_img.reshape(img_array.shape)
    # step that converts a numpy array into a PIL image.
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

    # to create a new array that has the same shape and type as flat_img, but filled with zeros.
    # to ensure that the newly creates array has the exactly same properties of the original flattened image.
    decrypted_flat_img = np.zeros_like(flat_img)
    decrypted_flat_img[swap_pattern] = flat_img

    decrypted_img_array = decrypted_flat_img.reshape(img_array.shape)
    decrypted_img = Image.fromarray(decrypted_img_array)

    decrypted_img_path = image_path.replace("_encrypted.", "_decrypted.")
    decrypted_img.save(decrypted_img_path)

    return decrypted_img, decrypted_img_path

#main body code
image_path = input(r'Enter path of Image : ')

# key for generating the swap pattern
key = int(input("Enter the Key: "))

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
