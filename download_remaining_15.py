import os
import urllib.request
import hashlib
from PIL import Image

TARGETS = {
    "products/product_30.png": "https://images.unsplash.com/photo-1547082299-de196ea013d6?w=1000&auto=format&fit=crop&q=85",
    "brands/brand_asus.png": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=1000&auto=format&fit=crop&q=85",
    "brands/brand_canon.png": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=1000&auto=format&fit=crop&q=85",
    "deals/offer_3.png": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_1.png": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_2.png": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_3.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1000&auto=format&fit=crop&q=85",
    "categories/compare_4.png": "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=1000&auto=format&fit=crop&q=85",
    "home/bento_acc.png": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=1000&auto=format&fit=crop&q=85",
    "home/smarthome_1.png": "https://images.unsplash.com/photo-1558002038-1055907df827?w=1000&auto=format&fit=crop&q=85",
    "home/smarthome_2.png": "https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_1.png": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_2.png": "https://images.unsplash.com/photo-1512446816042-444d641267d4?w=1000&auto=format&fit=crop&q=85",
    "home/showroom_3.png": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1000&auto=format&fit=crop&q=85",
    "home/latest_tech_1.png": "https://images.unsplash.com/photo-1511385342265-721787e8342f?w=1000&auto=format&fit=crop&q=85"
}

def main():
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    print(f"Fixing {len(TARGETS)} remaining assets with live valid URLs...")
    for rel_path, url in TARGETS.items():
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
            print(f"[OK] {rel_path}")
        except Exception as e:
            print(f"[FAIL] {rel_path}: {e}")

if __name__ == "__main__":
    main()
