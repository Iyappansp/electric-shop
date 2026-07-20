import urllib.request
import os
from PIL import Image

PHOTO_URLS = {
    # 9 target products requiring real photography photos
    "product_16.png": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80",  # ChronoLux Premium (Black Luxury Smartwatch)
    "product_36.png": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=800&auto=format&fit=crop&q=80",  # Apex Run Ultra (Fitness Smartwatch)
    "product_37.png": "https://images.unsplash.com/photo-1544117519-31a4b719223d?w=800&auto=format&fit=crop&q=80",  # Galaxy Watch Ultra 2 (Sleek Smartwatch)
    "product_14.png": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800&auto=format&fit=crop&q=80",  # AirWave Buds 2 (Wireless Earbuds)
    "product_19.png": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=800&auto=format&fit=crop&q=80",  # TitanForce Gaming (RGB Gaming PC Tower)
    "product_22.png": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800&auto=format&fit=crop&q=80",  # StreamCast Capture (Streaming Hardware)
    "product_8.png":  "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&auto=format&fit=crop&q=80",  # Pulse Lite 5G (Modern Smartphone)
    "product_2.png":  "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=800&auto=format&fit=crop&q=80",  # Vortex Gaming Laptop (Gaming Laptop)
    "product_29.png": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&auto=format&fit=crop&q=80",  # ThinkBook Studio 14 (Minimalist Laptop)
}

out_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images\products"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in PHOTO_URLS.items():
    dest_path = os.path.join(out_dir, filename)
    tmp_path = dest_path + ".download"
    print(f"Downloading real photo for {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(tmp_path, 'wb') as out_file:
            out_file.write(response.read())
            
        # Convert & process image with PIL
        with Image.open(tmp_path) as img:
            img = img.convert("RGB")
            img.save(dest_path, "PNG", quality=95)
            
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"Successfully saved real photo to {dest_path}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
