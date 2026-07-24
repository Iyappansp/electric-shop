import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Auditing links across {len(html_files)} HTML pages...\n")

broken_links = []
redirect_check = []

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all href="..."
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        # Ignore external links, javascript:, tel:, mailto:, #
        if href.startswith(('http://', 'https://', 'javascript:', 'tel:', 'mailto:', '#')):
            continue
        
        page = href.split('?')[0].split('#')[0]
        if not page:
            continue
            
        full_path = os.path.normpath(page)
        if not os.path.exists(full_path):
            broken_links.append((h, href, f"File {full_path} does not exist!"))
        else:
            redirect_check.append((h, href))

print(f"Total internal links checked: {len(redirect_check) + len(broken_links)}")

if broken_links:
    print("\nBROKEN LINKS DETECTED:")
    for src_file, link, reason in broken_links:
        print(f"  [BROKEN] {src_file} -> {link} ({reason})")
else:
    print("\nSUCCESS: 0 broken file links found!")
