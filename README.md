# Prodigy_CS_Task2
# Simple Image Encryption Tool - 👁️⃤ Pixel Manipulation for Image Encryption &amp; Decryption 
Internship Task 2 at Prodigy InfoTech

## Overview🧐
This repository contains three Python programs designed to encrypt and decrypt images using pixel manipulation techniques. The programs include pixel swapping and basic mathematical operations on pixel values to ensure the image data is protected. Users can easily encrypt and decrypt images using these methods.

## Theoretical Explanation

### 🛡️Cybersecurity Concepts
- **Encryption**🔐: The process of converting plaintext data into ciphertext to protect it from unauthorized access. In this context, we apply encryption to image data.
- **Decryption**🔓: The process of converting ciphertext back into plaintext, allowing authorized users to access the original data.
- **Symmetric Key Encryption**🗝️: A type of encryption where the same key is used for both encryption and decryption. The security of this method relies on keeping the key secret.

### ⚙ Image Encryption Techniques 
#### Pixel Swapping 🗘
This technique involves permuting the pixel values in an image based on a deterministic pattern generated from a key. The pattern ensures that the pixels are shuffled in a reproducible manner during both encryption and decryption.
1. **Generate Swap Pattern**: 
    - Use a seed value (key) to initialize the random number generator.
    - Generate a sequence of indices representing pixel positions.
    - Shuffle the sequence deterministically based on the key.
2. **Encrypt**:
    - Flatten the image into a one-dimensional array.
    - Apply the swap pattern to reorder the pixel values.
    - Reshape the array back to the original image dimensions.
3. **Decrypt**:
    - Flatten the encrypted image into a one-dimensional array.
    - Apply the inverse of the swap pattern to reorder the pixel values back to their original positions.
    - Reshape the array back to the original image dimensions.

#### Basic Mathematical Operations 🧮
This method involves performing simple mathematical operations (like XOR) on pixel values using a key. The same operation is applied to decrypt the image by using the same key.
1. **Encrypt**:
    - Convert the image to a byte array.
    - Perform the XOR operation on each byte of the image with the given key.
    - Save the modified byte array as the encrypted image.
2. **Decrypt**:
    - Convert the encrypted image to a byte array.
    - Perform the XOR operation on each byte of the image with the same key used for encryption.
    - Save the modified byte array as the decrypted image.

## 📌Software Requirements
- Python 3.x
- Required Python libraries: `numpy`, `Pillow` (PIL)
- An Integrated Development Environment (IDE) like PyCharm or VSCode

## 📌Hardware Requirements
- Any modern computer with at least 2GB of RAM
- Minimum of 200MB of free storage space

## 🎯Steps to Execute the Program
### Program 1: Pixel Swapping Encryption & Decryption
1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Program**:
   - Open `pixel_swap.py` in your Python IDE (e.g., PyCharm).
   - Execute the script and follow the prompts to enter the image path and the encryption key.

3. **Example Execution**:
   - Input Image Path: `example.png`
   - Key: 1234
   - The program will output encrypted and decrypted images in the same directory.

### Program 2: Encrypt an Image Using Simple Mathematical Logic
1. **Run the Program**:
   - Open `encrypt_image.py` in your Python IDE.
   - Execute the script and follow the prompts to enter the image path and the encryption key.

2. **Example Execution**:
   - Input Image Path: `example.png`
   - Key: 1234
   - The program will encrypt the image in-place.

### Program 3: Decrypt an Image Using Simple Mathematical Logic
1. **Run the Program**:
   - Open `decrypt_image.py` in your Python IDE.
   - Execute the script and follow the prompts to enter the image path and the decryption key.

2. **Example Execution**:
   - Input Image Path: `example_encrypted.png`
   - Key: 1234
   - The program will decrypt the image in-place.

## Thanks✨
I appreciate your usage of and contributions to this repository. 
Thank you for your attention, and I hope that these image encryption programs may be helpful to you in your cybersecurity learning.

## Contribute🤝
Welcome contributions to enhance these programs and expand their capabilities. 
To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your branch.
4. Open a pull request describing your changes.

⚠️Please ensure your code adheres to the existing style and includes appropriate documentation and tests.

🛡️Secure coding!🛡️
