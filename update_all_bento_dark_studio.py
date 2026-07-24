import os
import urllib.request
from PIL import Image

# Curated, 100% harmonized dark studio technology photography for all 6 category bento slots
DARK_STUDIO_BENTO = {
    # 1. Laptops - Dark neon ambient studio laptop
    "assets/images/home/bento_laptop.png": "https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1200&auto=format&fit=crop&q=90",
    
    # 2. Phones - Flagship smartphone on dark sleek studio surface
    "assets/images/home/bento_phone.png": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=1200&auto=format&fit=crop&q=90",
    
    # 3. Headphones - Audiophile headphones on dark studio background (NO bright yellow!)
    "assets/images/home/bento_audio.png": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=1200&auto=format&fit=crop&q=90",
    
    # 4. Smartwatches - Premium smartwatch showcase on dark background (NO outdoor wrist!)
    "assets/images/home/bento_watch.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1200&auto=format&fit=crop&q=90",
    
    # 5. Accessories - Tech accessories flatlay on dark slate background (NO white charger on desk!)
    "assets/images/home/bento_acc.png": "https://images.unsplash.com/photo-1609081219090-a6d81d3085bf?w=1200&auto=format&fit=crop&q=90",
    
    # 6. Gaming Zone - RGB battlestation on dark ambient background
    "assets/images/home/bento_game.png": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=1200&auto=format&fit=crop&q=90",
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def update_bento():
    for rel_path, url in DARK_STUDIO_BENTO.items():
        full_path = os.path.abspath(rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        tmp_path = full_path + ".tmp"
        print(f"Downloading dark studio asset for {rel_path}...")
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

if __name__ == "__main__":
    update_bento()
