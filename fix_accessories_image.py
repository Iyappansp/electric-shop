import os
import urllib.request
from PIL import Image

# 1. Update bento_acc.png, cat_accessories_hero.png, accessories_hero_bg.png with guaranteed 100% pure tech accessories (chargers, cables, power bank, USB-C hub)
ACC_URLS = {
    "assets/images/home/bento_acc.png": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=1200&auto=format&fit=crop&q=90",
    "assets/images/categories/cat_accessories_hero.png": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=1600&auto=format&fit=crop&q=90",
    "assets/images/categories/accessories_hero_bg.png": "https://images.unsplash.com/photo-1609081219090-a6d81d3085bf?w=1600&auto=format&fit=crop&q=90",
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for rel_path, url in ACC_URLS.items():
    full_path = os.path.abspath(rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    tmp_path = full_path + ".tmp"
    print(f"Downloading {rel_path}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(tmp_path, "wb") as f:
            f.write(resp.read())
            
        with Image.open(tmp_path) as img:
            img = img.convert("RGB")
            img.save(full_path, "PNG", quality=95)
            
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"[SUCCESS] Updated {rel_path} ({os.path.getsize(full_path)} bytes)")
    except Exception as e:
        print(f"[FAIL] {rel_path}: {e}")
