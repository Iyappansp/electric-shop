import os, shutil, glob, re
from bs4 import BeautifulSoup

project_dir = r'd:\mageten\electric-shop'
cta_dir = os.path.join(project_dir, 'assets', 'cta')
home_img_dir = os.path.join(project_dir, 'assets', 'images', 'home')

os.makedirs(cta_dir, exist_ok=True)
os.makedirs(home_img_dir, exist_ok=True)

# Define source images in assets/cta
source_images = {
    'cta_bg_1.png': os.path.join(cta_dir, 'image.png'),
    'cta_bg_2.png': os.path.join(cta_dir, 'image copy.png'),
    'cta_bg_3.png': os.path.join(cta_dir, 'image copy 2.png'),
    'cta_bg_4.png': os.path.join(cta_dir, 'image copy 3.png'),
    'cta_bg_5.png': os.path.join(cta_dir, 'image copy 4.png'),
    'cta_bg_6.png': os.path.join(cta_dir, 'image copy 5.png'),
    'cta_bg_7.png': os.path.join(cta_dir, 'image copy 6.png'),
}

# Create sanitized web-safe aliases inside assets/cta
for bg_name, src_path in source_images.items():
    if os.path.exists(src_path):
        target_path = os.path.join(cta_dir, bg_name)
        shutil.copy2(src_path, target_path)
        print(f"Copied {os.path.basename(src_path)} -> assets/cta/{bg_name}")

        # Also create snake_case filename without spaces inside assets/cta
        sanitized_name = os.path.basename(src_path).replace(' ', '_')
        if sanitized_name != os.path.basename(src_path):
            snake_path = os.path.join(cta_dir, sanitized_name)
            shutil.copy2(src_path, snake_path)
            print(f"Copied {os.path.basename(src_path)} -> assets/cta/{sanitized_name}")

# Mirror to assets/images/home/ for legacy fallbacks
legacy_mappings = {
    'newsletter_cta_bg.png': source_images['cta_bg_1.png'],
    'final_cta_bg.png': source_images['cta_bg_2.png'],
    'bulk_cta_bg.png': source_images['cta_bg_3.png'],
    'about_final_cta_bg.png': source_images['cta_bg_4.png'],
    'contact_cta_bg.png': source_images['cta_bg_5.png'],
    'compare_cta_bg.png': source_images['cta_bg_6.png'],
    'weekly_deals_hero_bg.png': source_images['cta_bg_7.png'],
}

for leg_name, src_path in legacy_mappings.items():
    if os.path.exists(src_path):
        target_path = os.path.join(home_img_dir, leg_name)
        shutil.copy2(src_path, target_path)
        print(f"Mirrored {os.path.basename(src_path)} -> assets/images/home/{leg_name}")

print("\n--- UPDATE CSS FILES ---")

# Update assets/css/home.css
home_css_path = os.path.join(project_dir, 'assets', 'css', 'home.css')
if os.path.exists(home_css_path):
    with open(home_css_path, 'r', encoding='utf-8') as f:
        css_text = f.read()
    
    # Update background-image URLs in home.css to use assets/cta
    css_text = re.sub(
        r"url\(['\"]?\.\./images/home/newsletter_cta_bg\.png['\"]?\)",
        "url('../cta/cta_bg_1.png')",
        css_text
    )
    css_text = re.sub(
        r"url\(['\"]?\.\./images/home/final_cta_bg\.png['\"]?\)",
        "url('../cta/cta_bg_2.png')",
        css_text
    )
    
    with open(home_css_path, 'w', encoding='utf-8') as f:
        f.write(css_text)
    print("Updated assets/css/home.css")

# Update assets/css/layout.css
layout_css_path = os.path.join(project_dir, 'assets', 'css', 'layout.css')
if os.path.exists(layout_css_path):
    with open(layout_css_path, 'r', encoding='utf-8') as f:
        css_text = f.read()
    
    # Ensure default .final-cta-section uses cta_bg_2.png from assets/cta
    if 'background-image' not in css_text or '.final-cta-section {' in css_text:
        css_text = re.sub(
            r'(\.final-cta-section\s*\{[^}]*)',
            r"\1\n  background-image: linear-gradient(rgba(10, 15, 28, 0.78), rgba(10, 15, 28, 0.9)), url('../cta/cta_bg_2.png');",
            css_text,
            count=1
        )
    with open(layout_css_path, 'w', encoding='utf-8') as f:
        f.write(css_text)
    print("Updated assets/css/layout.css")

print("\n--- UPDATE HTML FILES ---")

# Specific HTML page mapping for CTA background images
html_updates = {
    'index.html': [
        (r"style=[\"']background-image:[^\"']*newsletter_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(120deg, rgba(10,15,28,0.78), rgba(10,15,28,0.88)), url('assets/cta/cta_bg_1.png'); background-size:cover; background-position:center;\""),
        (r"style=[\"']background-image:[^\"']*final_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_2.png'); background-size:cover; background-position:center;\"")
    ],
    'home-2.html': [
        (r"style=[\"']background-image:[^\"']*bulk_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(120deg, rgba(10,15,28,0.78), rgba(10,15,28,0.88)), url('assets/cta/cta_bg_3.png'); background-size:cover; background-position:center;\"")
    ],
    'about.html': [
        (r"style=[\"']background-image:[^\"']*about_final_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_4.png'); background-size:cover; background-position:center;\"")
    ],
    'contact.html': [
        (r"style=[\"']background-image:[^\"']*contact_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_5.png'); background-size:cover; background-position:center;\"")
    ],
    'product-comparison.html': [
        (r"style=[\"']background-image:[^\"']*compare_cta_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_6.png'); background-size:cover; background-position:center;\"")
    ],
    'weekly-deals.html': [
        (r"style=[\"']background-image:[^\"']*weekly_deals_hero_bg[^\"']*[\"']", 
         "style=\"background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_7.png'); background-size:cover; background-position:center;\"")
    ]
}

for fname, replacements in html_updates.items():
    fpath = os.path.join(project_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        for pattern, repl in replacements:
            html = re.sub(pattern, repl, html)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated CTA background styles in {fname}")

print("\n--- CHECK ALL REMAINING HTML FILES FOR UNSET CTA BACKGROUNDS ---")
all_html = glob.glob(os.path.join(project_dir, '*.html'))
for hf in sorted(all_html):
    fname = os.path.basename(hf)
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace any leftover old image bg links with assets/cta links
    old_bg_patterns = [
        (r"assets/images/home/newsletter_cta_bg\.png", "assets/cta/cta_bg_1.png"),
        (r"assets/images/home/final_cta_bg\.png", "assets/cta/cta_bg_2.png"),
        (r"assets/images/home/bulk_cta_bg\.png", "assets/cta/cta_bg_3.png"),
        (r"assets/images/home/about_final_cta_bg\.png", "assets/cta/cta_bg_4.png"),
        (r"assets/images/home/contact_cta_bg\.png", "assets/cta/cta_bg_5.png"),
        (r"assets/images/home/compare_cta_bg\.png", "assets/cta/cta_bg_6.png"),
        (r"assets/images/home/weekly_deals_hero_bg\.png", "assets/cta/cta_bg_7.png"),
    ]
    
    modified = False
    for old_p, new_p in old_bg_patterns:
        if re.search(old_p, html):
            html = re.sub(old_p, new_p, html)
            modified = True
            
    if modified:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated legacy image references in {fname} to assets/cta/...")

print("\nAll CTA background updates executed successfully!")
