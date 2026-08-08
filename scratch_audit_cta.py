import glob

files = sorted(glob.glob('*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    cta_sec = 'final-cta-section' in content
    has_cont = False
    if cta_sec:
        pos = content.find('final-cta-section')
        snippet = content[pos:pos+150]
        has_cont = '<div class="container">' in snippet
    
    nl_band = 'newsletter-band' in content
    print(f"{f:25s} | CTA Sec: {str(cta_sec):5s} | Has Container: {str(has_cont):5s} | Newsletter Band: {nl_band}")
