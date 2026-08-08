import glob, os, re
from bs4 import BeautifulSoup

project_dir = r'd:\mageten\electric-shop'
html_files = sorted(glob.glob(os.path.join(project_dir, '*.html')))
css_files = sorted(glob.glob(os.path.join(project_dir, 'assets', 'css', '*.css')))

print("=== VERIFYING CTA BACKGROUND URLS IN HTML & CSS ===\n")

missing_files = []
found_cta_urls = []

def check_url(rel_url, source_file):
    # Strip gradient or external wrap if present
    clean_url = rel_url.strip("'\"")
    # Resolve path relative to source file directory
    if clean_url.startswith('../'):
        abs_path = os.path.normpath(os.path.join(os.path.dirname(source_file), clean_url))
    else:
        abs_path = os.path.normpath(os.path.join(project_dir, clean_url))
    
    exists = os.path.isfile(abs_path)
    print(f"File: {os.path.basename(source_file)} | URL: {clean_url} | Exists: {exists}")
    if not exists:
        missing_files.append((source_file, clean_url, abs_path))

print("--- HTML FILES ---")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(True):
        style = tag.get('style', '')
        if 'background-image' in style:
            urls = re.findall(r"url\(['\"]?([^'\"]+)['\"]?\)", style)
            for u in urls:
                if 'cta' in u.lower() or 'bg' in u.lower():
                    found_cta_urls.append((hf, u))
                    check_url(u, hf)

print("\n--- CSS FILES ---")
for cf in css_files:
    with open(cf, 'r', encoding='utf-8') as f:
        css = f.read()
    urls = re.findall(r"url\(['\"]?([^'\"]+)['\"]?\)", css)
    for u in urls:
        if 'cta' in u.lower() or 'bg' in u.lower():
            found_cta_urls.append((cf, u))
            check_url(u, cf)

print(f"\nTotal CTA / Background URLs checked: {len(found_cta_urls)}")
if missing_files:
    print(f"ERROR: Found {len(missing_files)} missing background image files!")
    for src, url, path in missing_files:
        print(f"  In {src}: {url} -> {path} NOT FOUND")
else:
    print("SUCCESS: 100% of CTA background image URLs resolve to existing, verified image files!")
