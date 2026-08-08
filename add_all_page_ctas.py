import os, re

project_dir = r'd:\mageten\electric-shop'

page_ctas = {
    'bulk-orders.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_3.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Ready to Equip Your Team or Organization?</h2>
        <p>Get custom volume quotes, dedicated account management, and tax-exempt processing today.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="#bulk-form" class="btn btn-primary btn-lg">Request Bulk Quote</a>
        <a href="contact.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Contact Enterprise Sales</a>
      </div>
    </section>
  </main>''',

    'faq.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_5.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Still Have Questions?</h2>
        <p>Our dedicated support specialists are available 24/7 to assist with your technical or order inquiries.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="contact.html" class="btn btn-primary btn-lg">Contact Support</a>
        <a href="store-locator.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Find Store Near You</a>
      </div>
    </section>
  </main>''',

    'store-locator.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_5.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Visit a Voltage Store Near You</h2>
        <p>Try out the latest flagship products in-person and get personalized recommendations from our tech experts.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="categories.html" class="btn btn-primary btn-lg">Browse Products</a>
        <a href="contact.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Get Directions & Hours</a>
      </div>
    </section>
  </main>''',

    'categories.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_1.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Looking for Something Specific?</h2>
        <p>Discover top-rated electronics, exclusive weekly deals, and certified brand-new devices.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">View Weekly Deals</a>
        <a href="product-comparison.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Compare Models</a>
      </div>
    </section>
  </main>''',

    'brands.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_2.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Shop 100% Authentic Brand Hardware</h2>
        <p>All items come with official manufacturer warranty and guaranteed authentic quality.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="categories.html" class="btn btn-primary btn-lg">Browse All Brands</a>
        <a href="contact.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Ask a Specialist</a>
      </div>
    </section>
  </main>'''
}

for fname, cta_code in page_ctas.items():
    fpath = os.path.join(project_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'final-cta-section' not in content:
            content = content.replace('</main>', cta_code)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added final CTA section with assets/cta background image to {fname}")
