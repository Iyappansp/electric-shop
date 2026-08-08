import glob

print("--- CTA & Eyebrow Alignment Verification ---")

# 1. Verify accessories.html
with open('accessories.html', 'r', encoding='utf-8') as f:
    acc_content = f.read()

assert 'class="final-cta-section"' in acc_content
assert '<div class="container">' in acc_content
print("[OK] accessories.html: container wrapper is present")

# 2. Verify home-2.html
with open('home-2.html', 'r', encoding='utf-8') as f:
    h2_content = f.read()

assert 'align-self:center' in h2_content or 'align-self: center' in h2_content
print("[OK] home-2.html: Eyebrow badge in bulk order band has align-self: center")

# 3. Verify CSS files
with open('assets/css/home.css', 'r', encoding='utf-8') as f:
    home_css = f.read()

assert '.newsletter-band .eyebrow' in home_css
print("[OK] home.css: .newsletter-band .eyebrow rule present")

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

assert '.section-head.center .eyebrow' in style_css
print("[OK] style.css: Centered eyebrow rules present")

with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    layout_css = f.read()

assert '.final-cta-section .container' in layout_css
print("[OK] layout.css: .final-cta-section .container responsive rules present")

print("\nALL VERIFICATION CHECKS PASSED PERFECTLY!")
