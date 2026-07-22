import os
import urllib.request
import hashlib
from PIL import Image

TARGETS = {
    "categories/compare_3.png": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_4.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1000&auto=format&fit=crop&q=85",
    "home/bulk_hero.png": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=1000&auto=format&fit=crop&q=85",
    "products/product_22.png": "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=1000&auto=format&fit=crop&q=85",
    "products/product_32.png": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=1000&auto=format&fit=crop&q=85"
}

def main():
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for rel_path, url in TARGETS.items():
        dest_path = os.path.join(base_dir, rel_path)
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
            print(f"[OK] {rel_path}")
        except Exception as e:
            print(f"[FAIL] {rel_path}: {e}")

if __name__ == "__main__":
    main()
