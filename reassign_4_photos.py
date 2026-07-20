import urllib.request
import os
from PIL import Image

# 4 Target products to reassign fresh real photography images
TARGET_PHOTOS = {
    "product_16.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1000&auto=format&fit=crop&q=85",  # ChronoLux Premium (Minimalist Luxury Smartwatch)
    "product_29.png": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=1000&auto=format&fit=crop&q=85",  # ThinkBook Studio 14 (Sleek Studio Laptop)
    "product_14.png": "https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=1000&auto=format&fit=crop&q=85",  # AirWave Buds 2 (White TWS Earbuds & Case)
    "product_35.png": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=1000&auto=format&fit=crop&q=85",  # ROG Swift 360Hz (High-Refresh Gaming Monitor)
}

out_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images\products"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in TARGET_PHOTOS.items():
    dest_path = os.path.join(out_dir, filename)
    
    # 1. Remove previous image if exists
    if os.path.exists(dest_path):
        try:
            os.remove(dest_path)
            print(f"Removed previous image: {dest_path}")
        except Exception as err:
            print(f"Notice when deleting {dest_path}: {err}")
            
    tmp_path = dest_path + ".newtmp"
    print(f"Downloading new fresh real photo for {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(tmp_path, 'wb') as out_file:
            out_file.write(response.read())
            
        with Image.open(tmp_path) as img:
            img = img.convert("RGB")
            img.save(dest_path, "PNG", quality=95)
            
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"Successfully reassigned new photo for {filename} -> {dest_path}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
