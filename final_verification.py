import os
import re
from PIL import Image

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')] + ['assets/js/products.js']
total_imgs = 0
errors = []
unique_referenced_files = set()

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = [m for m in re.findall(r'assets/images/[^\s"\'\)]+', content) if '${' not in m]
    for m in matches:
        clean_m = m.split('?')[0].split('#')[0]
        total_imgs += 1
        unique_referenced_files.add(clean_m)
        full_p = os.path.normpath(clean_m)
        if not os.path.exists(full_p):
            errors.append(f"Missing image in {filepath}: {clean_m}")
        else:
            try:
                with Image.open(full_p) as im:
                    im.verify()
            except Exception as e:
                errors.append(f"Corrupt image in {filepath}: {clean_m} - {e}")

print(f"Total image references checked across HTML/JS: {total_imgs}")
print(f"Unique image files referenced: {len(unique_referenced_files)}")
if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  " + e)
else:
    print("ALL VERIFICATIONS PASSED SUCCESSFULLY! 100% of image references are valid, uncorrupted, and existing on disk.")
