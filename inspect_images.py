import os
import hashlib

base_dir = r"d:\mageten\electric-shop\assets\images"

for root, dirs, files in os.walk(base_dir):
    for f in sorted(files):
        if f.endswith((".png", ".jpg", ".webp")):
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, base_dir)
            size = os.path.getsize(fp)
            with open(fp, "rb") as img_file:
                h = hashlib.md5(img_file.read()).hexdigest()[:8]
            print(f"{rel:50s} | {size:8d} bytes | md5:{h}")
