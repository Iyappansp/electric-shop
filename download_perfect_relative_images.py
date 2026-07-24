import os
import hashlib
import urllib.request
from PIL import Image

# Curated, guaranteed 100% relevant high-resolution tech photography from Unsplash
IMAGE_UPDATES = {
    # 1. Bento Category Cards (Homepage)
    "assets/images/home/bento_acc.png": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1200&auto=format&fit=crop&q=90", # Sleek tech accessories, power bank, USB-C chargers & cables
    "assets/images/home/bento_laptop.png": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=1200&auto=format&fit=crop&q=90", # Modern laptop on sleek desk
    "assets/images/home/bento_phone.png": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1200&auto=format&fit=crop&q=90", # Sleek smartphone product photography
    "assets/images/home/bento_audio.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1200&auto=format&fit=crop&q=90", # Premium over-ear headphones
    "assets/images/home/bento_watch.png": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=1200&auto=format&fit=crop&q=90", # Modern smartwatch
    "assets/images/home/bento_game.png": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200&auto=format&fit=crop&q=90", # Battlestation RGB gaming setup

    # 2. Category Hero & Banners
    "assets/images/categories/cat_accessories_hero.png": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=1600&auto=format&fit=crop&q=90", # Premium tech accessories hero banner
    "assets/images/categories/accessories_hero_bg.png": "https://images.unsplash.com/photo-1609081219090-a6d81d3085bf?w=1600&auto=format&fit=crop&q=90", # Tech gadgets studio hero background
    "assets/images/categories/cat_laptop_hero.png": "https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1600&auto=format&fit=crop&q=90", # Laptop tech studio
    "assets/images/categories/cat_phone_hero.png": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=1600&auto=format&fit=crop&q=90", # Smartphone showcase
    "assets/images/categories/cat_headphones_hero.png": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=1600&auto=format&fit=crop&q=90", # Audiophile headphones studio
    "assets/images/categories/cat_smartwatches_hero.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1600&auto=format&fit=crop&q=90", # Smartwatch studio display
    "assets/images/categories/cat_gaming_hero.png": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=1600&auto=format&fit=crop&q=90", # Pro gaming rig hero banner
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def download_and_convert(rel_path, url):
    full_path = os.path.abspath(rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    tmp_path = full_path + ".tmp"
    
    print(f"Updating {rel_path}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(tmp_path, "wb") as f:
        f.write(resp.read())
        
    with Image.open(tmp_path) as img:
        img = img.convert("RGB")
        img.save(full_path, "PNG", quality=95)
        
    if os.path.exists(tmp_path):
        os.remove(tmp_path)
    print(f"[SUCCESS] Updated {rel_path} ({os.path.getsize(full_path)} bytes)")

if __name__ == "__main__":
    for rel_path, url in IMAGE_UPDATES.items():
        try:
            download_and_convert(rel_path, url)
        except Exception as e:
            print(f"[FAIL] Failed for {rel_path}: {e}")
