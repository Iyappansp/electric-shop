import urllib.request
import os
from PIL import Image

BENTO_PHOTOS = {
    "bento_laptop.png": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=1200&auto=format&fit=crop&q=90", # Sleek Laptop
    "bento_phone.png": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1200&auto=format&fit=crop&q=90",  # Smartphone
    "bento_audio.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1200&auto=format&fit=crop&q=90",  # Premium Headphones
    "bento_game.png": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200&auto=format&fit=crop&q=90",   # RGB Gaming Zone
    "bento_watch.png": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=1200&auto=format&fit=crop&q=90",  # Smartwatch
    "bento_acc.png": "https://images.unsplash.com/photo-1625772299848-391b6a87d7b3?w=1200&auto=format&fit=crop&q=90",    # Tech Accessories
}

out_dir = r"d:\mageten\electric-shop\assets\images\home"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

os.makedirs(out_dir, exist_ok=True)

for filename, url in BENTO_PHOTOS.items():
    dest_path = os.path.join(out_dir, filename)
    tmp_path = dest_path + ".download"
    print(f"Downloading bento image {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(tmp_path, 'wb') as out_file:
            out_file.write(response.read())
            
        with Image.open(tmp_path) as img:
            img = img.convert("RGB")
            img.save(dest_path, "PNG", quality=95)
            
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"Successfully updated {dest_path}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
