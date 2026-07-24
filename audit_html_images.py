import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
img_refs = set()

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(r'(?:src=["\']|url\(["\']?)(assets/images/[^\s"\')]+)', content)
        for m in matches:
            img_refs.add((h, m))

print(f"Total HTML image references found: {len(img_refs)}")
missing = []
existing = []
for page, ref in sorted(img_refs):
    # Clean ref in case of trailing query or fragment
    clean_ref = ref.split('?')[0].split('#')[0]
    full_p = os.path.normpath(clean_ref)
    if not os.path.exists(full_p):
        missing.append((page, clean_ref))
    else:
        existing.append((page, clean_ref, os.path.getsize(full_p)))

print(f"Existing references: {len(existing)}")
print(f"Missing references: {len(missing)}")
for page, ref in missing:
    print(f"  [MISSING] {page} -> {ref}")

print("\nSample of existing images:")
for page, ref, size in existing[:15]:
    print(f"  [OK] {page} -> {ref} ({size} bytes)")
