import os
import urllib.request
import hashlib
from PIL import Image

# 14 BRAND NEW UNIQUE UNSPLASH PHOTO URLS FOR ZERO-DUPLICATE GUARANTEE

NEW_PHOTOS = {
    "deals/clearance_1.png": "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=1000&auto=format&fit=crop&q=85",
    "deals/offer_3.png": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1000&auto=format&fit=crop&q=85",
    "home/bulk_hero.png": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_2.png": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_3.png": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_1.png": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_3.png": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_4.png": "https://images.unsplash.com/photo-1509741102003-ca64bfe5f069?w=1000&auto=format&fit=crop&q=85",
    "home/bento_acc.png": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=1000&auto=format&fit=crop&q=85",
    "home/smarthome_1.png": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1000&auto=format&fit=crop&q=85",
    "brands/brand_asus.png": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1000&auto=format&fit=crop&q=85",
    "home/smarthome_2.png": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1000&auto=format&fit=crop&q=85",
    "products/product_35.png": "https://images.unsplash.com/photo-1547119957-637f8679db1e?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_2.png": "https://images.unsplash.com/photo-1574944985070-8f30c4397291?w=1000&auto=format&fit=crop&q=85"
}

def main():
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    print(f"Replacing {len(NEW_PHOTOS)} duplicate photos with unique real-world tech photos...")
    for rel_path, url in NEW_PHOTOS.items():
        dest_path = os.path.join(base_dir, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        tmp_path = dest_path + ".tmp"
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                content = response.read()
            with open(tmp_path, 'wb') as out_file:
                out_file.write(content)
            with Image.open(tmp_path) as img:
                img = img.convert("RGB")
                img.save(dest_path, "PNG", quality=95)
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            print(f"[OK] Replaced with unique photo -> {rel_path}")
        except Exception as e:
            print(f"[FAIL] {rel_path}: {e}")

if __name__ == "__main__":
    main()
