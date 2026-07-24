import os
import urllib.request
from PIL import Image

DEALS_AND_BRANDS = {
    # Weekly & Special Deals
    "assets/images/deals/offer_1.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1000&auto=format&fit=crop&q=90", # Flash Sale Headphones
    "assets/images/deals/offer_2.png": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=1000&auto=format&fit=crop&q=90", # Student Offer Laptop
    "assets/images/deals/offer_3.png": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=1000&auto=format&fit=crop&q=90", # Bundle Deal Watch + Buds
    "assets/images/deals/deal_1.png": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=1000&auto=format&fit=crop&q=90", # Gaming Laptop Deal
    "assets/images/deals/deal_2.png": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=1000&auto=format&fit=crop&q=90", # Flagship Phone Deal
    "assets/images/deals/deal_3.png": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=1000&auto=format&fit=crop&q=90", # Studio Headphone Deal
    "assets/images/deals/deal_4.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1000&auto=format&fit=crop&q=90", # Smartwatch Deal
    "assets/images/deals/deal_5.png": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=1000&auto=format&fit=crop&q=90", # 240Hz Gaming Monitor Deal
    "assets/images/deals/deal_6.png": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=1000&auto=format&fit=crop&q=90", # Mechanical Keyboard Deal

    # Brand Spotlights
    "assets/images/brands/brand_apple.png": "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=1200&auto=format&fit=crop&q=90", # Apple Ecosystem
    "assets/images/brands/brand_apple_spotlight.png": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=1600&auto=format&fit=crop&q=90", # Apple MacBook Spotlight
    "assets/images/brands/brand_asus.png": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=1200&auto=format&fit=crop&q=90", # ASUS ROG Gaming
    "assets/images/brands/brand_rog_spotlight.png": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1600&auto=format&fit=crop&q=90", # ROG Battlestation Spotlight
    "assets/images/brands/brand_sony.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1200&auto=format&fit=crop&q=90", # Sony Audio
    "assets/images/brands/brand_samsung.png": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1200&auto=format&fit=crop&q=90", # Samsung Mobile
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def update_deals_and_brands():
    for rel_path, url in DEALS_AND_BRANDS.items():
        full_path = os.path.abspath(rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        tmp_path = full_path + ".tmp"
        print(f"Updating {rel_path}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp, open(tmp_path, "wb") as f:
                f.write(resp.read())
            
            with Image.open(tmp_path) as img:
                img = img.convert("RGB")
                img.save(full_path, "PNG", quality=95)
                
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            print(f"[SUCCESS] {rel_path} updated ({os.path.getsize(full_path)} bytes)")
        except Exception as e:
            print(f"[FAIL] {rel_path} failed: {e}")

if __name__ == "__main__":
    update_deals_and_brands()
