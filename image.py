import requests
import os
import uuid
import urllib.parse

# === Config ===
API_KEY = "ubQ6tF25ZD_h2k2Q"  # ganti dengan token kamu sendiri
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# === Helper ===
def generate_image_name(ext=".jpg"):
    """Generate unique random name untuk image (short UUID + ekstensi)"""
    unique_id = uuid.uuid4().hex[:8]
    return f"{unique_id}{ext}"

def save_image_from_url(url, save_name, folder="downloads"):
    """Download image dari URL dan simpan ke folder"""
    os.makedirs(folder, exist_ok=True)
    save_path = os.path.join(folder, save_name)
    try:
        response = requests.get(url, headers=HEADERS, stream=True, timeout=20)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"📥 Gambar berhasil diunduh: {save_path}")
        return save_path
    except requests.exceptions.RequestException as e:
        print(f"❌ Gagal download gambar: {e}")
        return None

# === Core Function: Image-to-Image (I2I) ===
def image_to_image(image_url, prompt, model="kontext"):
    """
    Transform image dengan prompt tambahan (I2I) menggunakan Pollinations.
    """
    # encode prompt supaya URL aman
    prompt_encoded = urllib.parse.quote(prompt)
    api_url = f"https://image.pollinations.ai/prompt/{prompt_encoded}?model={model}&image={image_url}"

    # nama file hasil
    save_name = generate_image_name(".png")
    save_path = save_image_from_url(api_url, save_name)

    return save_path

# === Manual Input Mode ===
if __name__ == "__main__":
    print("=== 🎨 Image-to-Image (Pollinations) ===")
    image_input = input("Masukkan URL gambar sumber: ").strip()
    prompt = input("Masukkan prompt transformasi: ").strip()

    result_path = image_to_image(image_input, prompt)
    if result_path:
        print(f"\n✅ Hasil I2I tersimpan di: {result_path}")
    else:
        print("❌ Gagal melakukan transformasi gambar.")
