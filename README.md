# Image-Encryption-Tool-using-Python

A simple image encryption project using Python and the Pillow library.

It allows users to:
- Encrypt an image by shifting the RGB values of each pixel.
- Decrypt the image back using the same numeric key.

This tool **does not use any real cryptography** — it's more of a visual obfuscation method that helps understand how digital images work under the hood.

📌 Why I Built This

My curiosity about how images store data and how we can manipulate pixel values grew as I studied Python and cybersecurity concepts

This small project was created to teach you how to process images, manipulate pixels, and comprehend how encryption-like logic functions in pictures.

🛠️ How It Works

- Encrypt: This adds a key value to the RGB (Red, Green, and Blue) components of each pixel.
- Decrypt: To recover the image, subtract the same key from each RGB component.

To stay within acceptable color ranges, the operation makes use of modulo 256.

▶️ How to Run

1. Install the required library
   
        pip install pillow

2. Run the script

       python project2.py

3. Follow the menu:
    === Image Encryption Tool ===
    1. Encrypt Image
    2. Decrypt Image
   Choose (1/2):

⚠️ Limitations

   - Not secure for real-world encryption.

   - Works only on RGB images

   - Use .png or .bmp formats for better results (JPEG can distort pixels due to compression).






