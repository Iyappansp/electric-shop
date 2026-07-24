import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

category_meta_map = {
    'accessories.html': 'assets/images/categories/cat_accessories_hero.png',
    'laptops.html': 'assets/images/categories/cat_laptop_hero.png',
    'smartphones.html': 'assets/images/categories/cat_phone_hero.png',
    'headphones.html': 'assets/images/categories/cat_headphones_hero.png',
    'smartwatches.html': 'assets/images/categories/cat_smartwatches_hero.png',
    'gaming.html': 'assets/images/categories/cat_gaming_hero.png',
}

for page, correct_img in category_meta_map.items():
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace og:image and twitter:image content if incorrect
        updated = re.sub(
            r'(<meta property="og:image" content=")[^"]+(">)',
            rf'\g<1>{correct_img}\g<2>',
            content
        )
        updated = re.sub(
            r'(<meta name="twitter:image" content=")[^"]+(">)',
            rf'\g<1>{correct_img}\g<2>',
            updated
        )
        
        if updated != content:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"[FIXED] Updated meta images on {page} -> {correct_img}")
        else:
            print(f"[OK] {page} meta images already correct")
