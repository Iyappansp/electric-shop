import os

project_dir = r'd:\mageten\electric-shop'

category_ctas = {
    'laptops.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_4.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Need Help Choosing the Right Laptop?</h2>
        <p>Compare workstation specs, gaming GPU benchmarks, or speak with an expert tech advisor.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="product-comparison.html" class="btn btn-primary btn-lg">Compare Laptops</a>
        <a href="contact.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Ask a Laptop Advisor</a>
      </div>
    </section>
  </main>''',

    'smartphones.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_5.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Upgrade Your Mobile Experience</h2>
        <p>Get up to $200 instant trade-in value on eligible devices with free express shipping.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">View Mobile Deals</a>
        <a href="product-comparison.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Compare Phones</a>
      </div>
    </section>
  </main>''',

    'headphones.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_1.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Experience Studio-Grade Audio</h2>
        <p>Immerse yourself in active noise cancellation, lossless playback, and high-fidelity sound.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">Shop Audio Deals</a>
        <a href="contact.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Audio Help</a>
      </div>
    </section>
  </main>''',

    'gaming.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_7.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Dominate the Leaderboard with Voltage Gaming Gear</h2>
        <p>High-refresh monitors, mechanical keyboards, and ultra-fast RTX rigs backed by 2-year warranty.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">View Gaming Deals</a>
        <a href="product-comparison.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Compare Gear</a>
      </div>
    </section>
  </main>''',

    'smartwatches.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_6.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Track Fitness, Health, and Daily Connectivity</h2>
        <p>Explore smartwatch bands, heart-rate tracking, and cellular GPS models with instant trade-in bonus.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">Shop Smartwatch Deals</a>
        <a href="categories.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">View All Wearables</a>
      </div>
    </section>
  </main>''',

    'accessories.html': '''    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta-section" data-reveal="fade" style="background-image:linear-gradient(rgba(10,15,28,0.78), rgba(10,15,28,0.9)), url('assets/cta/cta_bg_2.png'); background-size:cover; background-position:center;">
      <div class="final-cta-section__content">
        <h2>Complete Your Tech Setup with Voltage Accessories</h2>
        <p>Fast GaN chargers, braided USB-C cables, ergonomic stands, and protective cases.</p>
      </div>
      <div class="final-cta-section__actions">
        <a href="weekly-deals.html" class="btn btn-primary btn-lg">View Accessories Deals</a>
        <a href="categories.html" class="btn btn-secondary btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.35);">Browse All Setup Essentials</a>
      </div>
    </section>
  </main>'''
}

for fname, cta_code in category_ctas.items():
    fpath = os.path.join(project_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'final-cta-section' not in content:
            content = content.replace('</main>', cta_code)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added final CTA section to {fname}")
