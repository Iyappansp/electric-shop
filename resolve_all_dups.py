import os
import urllib.request
import hashlib
from PIL import Image

# Curated pool of high quality technology photo URLs
POOL = [
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1496065187959-7f07b8353c55?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1000&auto=format&fit=crop&q=85",
    "https://images.unsplash.com/photo-1504610926078-a1611febcad3?w=1000&auto=format&fit=crop&q=85"
]

def main():
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    hashes = {}
    pool_idx = 0

    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith((".png", ".jpg", ".jpeg")):
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, base_dir)
                with open(fp, "rb") as img_file:
                    content = img_file.read()
                    h = hashlib.md5(content).hexdigest()

                if h in hashes:
                    print(f"Resolving duplicate: {rel} (was duplicate of {hashes[h]})")
                    while pool_idx < len(POOL):
                        url = POOL[pool_idx]
                        pool_idx += 1
                        try:
                            req = urllib.request.Request(url, headers=headers)
                            with urllib.request.urlopen(req) as resp:
                                new_data = resp.read()
                            new_h = hashlib.md5(new_data).hexdigest()
                            if new_h not in hashes:
                                tmp_p = fp + ".tmp"
                                with open(tmp_p, "wb") as out:
                                    out.write(new_data)
                                with Image.open(tmp_p) as img:
                                    img.convert("RGB").save(fp, "PNG", quality=95)
                                if os.path.exists(tmp_p):
                                    os.remove(tmp_p)
                                hashes[new_h] = rel
                                print(f"  -> Successfully replaced {rel} with unique photo ({new_h[:8]})")
                                break
                        except Exception as e:
                            print(f"  -> Pool URL failed: {e}")
                else:
                    hashes[h] = rel

    print("\nResolution finished.")

if __name__ == "__main__":
    main()
