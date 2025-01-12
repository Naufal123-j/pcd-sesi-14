import imageio
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk mengenkripsi citra menggunakan XOR
def encrypt_image(image, key):
    """
    Mengenkripsi citra menggunakan operasi XOR.

    Parameters:
    - image: Array numpy dari citra asli.
    - key: Nilai integer (kunci) untuk operasi XOR.

    Returns:
    - encrypted_image: Citra terenkripsi dalam bentuk array numpy.
    """
    encrypted_image = np.bitwise_xor(image, key)
    return encrypted_image

# Fungsi utama
def main():
    # Membaca citra asli
    image_path = "C:\gambar\download.webp"  # Ganti dengan path citra Anda
    image = imageio.imread(image_path)

    # Pastikan citra dalam format grayscale jika diperlukan
    if len(image.shape) == 3:
        image = np.mean(image, axis=2).astype(np.uint8)

    # Menentukan kunci untuk enkripsi
    key = 123  # Kunci enkripsi, harus disimpan untuk dekripsi

    # Mengenkripsi citra
    encrypted_image = encrypt_image(image, key)

    # Menampilkan citra asli dan citra terenkripsi
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Encrypted Image")
    plt.imshow(encrypted_image, cmap="gray")
    plt.axis("off")

    plt.show()

    # Menyimpan citra terenkripsi
    encrypted_image_path = "encrypted_image.png"
    imageio.imwrite(encrypted_image_path, encrypted_image)
    print(f"Encrypted image saved to {encrypted_image_path}")

if __name__ == "__main__":
    main()
