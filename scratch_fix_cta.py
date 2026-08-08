import glob
import re

files = glob.glob('*.html')

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'final-cta-section' not in content:
        continue

    # Check if section has container
    # Match <section class="final-cta-section"...> to </section>
    pos = content.find('final-cta-section')
    sec_start = content.rfind('<section', 0, pos)
    sec_end = content.find('</section>', sec_start) + len('</section>')
    
    sec_html = content[sec_start:sec_end]
    
    if '<div class="container">' not in sec_html:
        print(f"Updating {f}...")
        # Insert <div class="container"> after opening <section...> tag
        first_gt = sec_html.find('>')
        opening_tag = sec_html[:first_gt+1]
        closing_tag = '</section>'
        inner_content = sec_html[first_gt+1:-len(closing_tag)]
        
        new_sec_html = f"{opening_tag}\n      <div class=\"container\">\n{inner_content}      </div>\n    {closing_tag}"
        
        new_content = content[:sec_start] + new_sec_html + content[sec_end:]
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"  Fixed {f}")
    else:
        print(f"Skipping {f} (already has container)")
