import os
import urllib.request

SHOWROOM_PHOTOS = {
    "assets/images/home/showroom_1.png": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=1000&auto=format&fit=crop&q=85",
    "assets/images/home/showroom_2.png": "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=1000&auto=format&fit=crop&q=85"
}

def download_images():
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for rel_path, url in SHOWROOM_PHOTOS.items():
        dest_path = os.path.join(base_dir, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        print(f"Downloading {rel_path} from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(dest_path, "wb") as f:
                f.write(data)
        print(f"Successfully downloaded {rel_path} ({len(data)} bytes).")

if __name__ == "__main__":
    download_images()
