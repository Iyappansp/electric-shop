import urllib.request
import os
from PIL import Image

SMARTHOME_PHOTOS = {
    "smarthome_1.png": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=1000&auto=format&fit=crop&q=85", # Smart Home Hub / Speaker
    "smarthome_2.png": "https://images.unsplash.com/photo-1558002038-1055907df827?w=1000&auto=format&fit=crop&q=85", # Smart Home Controller / Lighting
}

out_dir = r"d:\mageten\electric-shop\assets\images\home"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

os.makedirs(out_dir, exist_ok=True)

for filename, url in SMARTHOME_PHOTOS.items():
    dest_path = os.path.join(out_dir, filename)
    tmp_path = dest_path + ".download"
    print(f"Downloading smart home photo {filename}...")
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
