from PIL import Image

def encrypted_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            #  basic mathematical operation for encryption
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    img.save(output_path)
    print(f"Encrypted image saved to: {output_path}")


def decrypted_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reverse the encryption  method
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    img.save(output_path)
    print(f"Decrypted image saved to: {output_path}")


def main():
    print("=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose (1/2): ")
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption key (number): "))

    if choice == '1':
        encrypted_image(input_path, output_path, key)
    elif choice == '2':
        decrypted_image(input_path, output_path, key)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
