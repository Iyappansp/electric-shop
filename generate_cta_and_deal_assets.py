import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def draw_radial_gradient(draw, width, height, center_x, center_y, radius, color_center, color_outer):
    for r in range(radius, 0, -4):
        t = r / radius
        r_col = int(color_center[0] * (1 - t) + color_outer[0] * t)
        g_col = int(color_center[1] * (1 - t) + color_outer[1] * t)
        b_col = int(color_center[2] * (1 - t) + color_outer[2] * t)
        a_col = int(color_center[3] * (1 - t) + color_outer[3] * t) if len(color_center) > 3 else 255
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(r_col, g_col, b_col, a_col))

def create_studio_bg(width=1280, height=960, c1=(0, 240, 255), c2=(138, 43, 226), bg_color=(8, 12, 22)):
    img = Image.new("RGBA", (width, height), (*bg_color, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    
    draw_radial_gradient(gdraw, width, height, int(width * 0.3), int(height * 0.35), int(min(width, height) * 0.65), (*c1, 120), (*bg_color, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.7), int(height * 0.65), int(min(width, height) * 0.7), (*c2, 110), (*bg_color, 0))
    
    glow = glow.filter(ImageFilter.GaussianBlur(radius=50))
    img.alpha_composite(glow)
    
    draw = ImageDraw.Draw(img, "RGBA")
    grid_step = 60
    for x in range(0, width, grid_step):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 12), width=1)
    for y in range(0, height, grid_step):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 12), width=1)
        
    return img, draw

def save_supersampled(img, filepath, target_w=640, target_h=480):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    img_resized.save(filepath, "PNG", quality=95)
    print(f"Generated asset: {filepath}")

# ----------------- CTA BACKGROUNDS -----------------

def gen_cta_bg(filepath, title="VOLTAGE", c1=(0, 240, 255), c2=(138, 43, 226)):
    w, h = 1920, 800
    img = Image.new("RGBA", (w, h), (10, 15, 28, 255))
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    
    draw_radial_gradient(gdraw, w, h, int(w * 0.25), int(h * 0.4), 600, (*c1, 140), (10, 15, 28, 0))
    draw_radial_gradient(gdraw, w, h, int(w * 0.75), int(h * 0.6), 650, (*c2, 130), (10, 15, 28, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
    img.alpha_composite(glow)
    
    draw = ImageDraw.Draw(img, "RGBA")
    # Add tech mesh and circuit accents
    for x in range(0, w, 80):
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 15), width=1)
    for y in range(0, h, 80):
        draw.line([(0, y), (w, y)], fill=(255, 255, 255, 15), width=1)
        
    # Floating circuit nodes
    for i in range(12):
        nx = (i * 170 + 80) % w
        ny = (i * 130 + 50) % h
        draw.ellipse([nx-6, ny-6, nx+6, ny+6], fill=(*c1, 200), outline=(255, 255, 255, 255), width=2)
        draw.line([(nx, ny), (nx + 40, ny + 30)], fill=(*c1, 100), width=2)
        
    save_supersampled(img, filepath, 1280, 500)

# ----------------- MONITORS (product_20 & product_35) -----------------

def gen_pixelview_27(filepath):
    # ID 20: PixelView 27" 240Hz Gaming Monitor
    img, draw = create_studio_bg(1280, 960, (0, 210, 255), (120, 50, 255))
    cx, cy = 640, 420
    
    # Stand base
    draw.polygon([(cx - 180, cy + 340), (cx + 180, cy + 340), (cx + 100, cy + 280), (cx - 100, cy + 280)], fill=(25, 30, 42, 255), outline=(0, 210, 255, 180), width=3)
    # Stand column
    draw.rectangle([cx - 28, cy + 180, cx + 28, cy + 300], fill=(35, 42, 58, 255), outline=(60, 70, 90, 255), width=2)
    
    # Monitor Outer Frame / Bezel (27" 16:9 aspect ratio)
    mw, mh = 880, 500
    draw.rounded_rectangle([cx - mw//2, cy - mh//2, cx + mw//2, cy + mh//2], radius=16, fill=(15, 18, 26, 255), outline=(0, 210, 255, 220), width=5)
    
    # Screen Display Area
    sw, sh = 850, 470
    draw.rounded_rectangle([cx - sw//2, cy - sh//2, cx + sw//2, cy + sh//2], radius=10, fill=(6, 10, 20, 255))
    
    # Wallpaper artwork on screen (Futuristic neon game scene)
    s_left, s_top = cx - sw//2, cy - sh//2
    # Cyberpunk mountain / grid horizon on monitor
    draw.polygon([(s_left, cy + 180), (cx - 150, cy - 20), (cx + 50, cy + 80), (cx + 250, cy - 80), (s_left + sw, cy + 180)], fill=(30, 15, 60, 255))
    draw.polygon([(cx - 200, cy + 180), (cx + 20, cy - 60), (cx + 220, cy + 180)], fill=(0, 180, 240, 180))
    # Sun disk
    draw.ellipse([cx - 70, cy - 110, cx + 70, cy + 30], fill=(255, 0, 128, 230))
    # Perspective grid lines on display floor
    for gx in range(s_left, s_left + sw, 40):
        draw.line([(gx, cy + 80), (cx + (gx - cx)*2, cy + sh//2)], fill=(0, 240, 255, 90), width=2)
    for gy in range(cy + 80, cy + sh//2, 25):
        draw.line([(s_left, gy), (s_left + sw, gy)], fill=(255, 0, 128, 70), width=2)
        
    # Brand logo on bottom chin
    draw.text((cx - 40, cy + mh//2 - 18), "PIXELVIEW", fill=(200, 230, 255, 200))
    
    # Power LED glow dot
    draw.ellipse([cx + mw//2 - 35, cy + mh//2 - 12, cx + mw//2 - 25, cy + mh//2 - 2], fill=(0, 255, 200, 255))
    
    save_supersampled(img, filepath, 640, 480)

def gen_rog_swift_360(filepath):
    # ID 35: ROG Swift 360Hz Gaming Monitor
    img, draw = create_studio_bg(1280, 960, (255, 0, 100), (0, 240, 255))
    cx, cy = 640, 420
    
    # V-shaped tripod gaming stand
    draw.polygon([(cx, cy + 200), (cx - 240, cy + 340), (cx - 180, cy + 340), (cx, cy + 230)], fill=(40, 45, 60, 255), outline=(255, 0, 100, 200), width=2)
    draw.polygon([(cx, cy + 200), (cx + 240, cy + 340), (cx + 180, cy + 340), (cx, cy + 230)], fill=(40, 45, 60, 255), outline=(255, 0, 100, 200), width=2)
    draw.rectangle([cx - 30, cy + 160, cx + 30, cy + 260], fill=(30, 35, 48, 255), outline=(0, 240, 255, 200), width=2)
    
    # Frameless ultra-thin bezel 27" 360Hz Monitor
    mw, mh = 890, 510
    draw.rounded_rectangle([cx - mw//2, cy - mh//2, cx + mw//2, cy + mh//2], radius=14, fill=(12, 14, 22, 255), outline=(255, 0, 100, 220), width=4)
    
    sw, sh = 864, 484
    draw.rounded_rectangle([cx - sw//2, cy - sh//2, cx + sw//2, cy + sh//2], radius=8, fill=(4, 6, 14, 255))
    
    # Screen artwork - 360Hz esports motion graphic
    for r in range(350, 50, -40):
        draw.ellipse([cx - r, cy - r//2, cx + r, cy + r//2], outline=(0, 240, 255, 120), width=3)
    draw.text((cx - 80, cy - 20), "360Hz ESPORTS", fill=(255, 255, 255, 240))
    draw.text((cx - 60, cy + 20), "0.5ms ULMB 2", fill=(255, 0, 100, 240))
    
    save_supersampled(img, filepath, 640, 480)

# ----------------- BUNDLE CARDS (bundle_1 to bundle_4) -----------------

def gen_bundle_1(filepath):
    # Creator Studio Pro Bundle: Studio Laptop + 27" 4K Monitor + SSD
    img, draw = create_studio_bg(1280, 960, (0, 240, 255), (147, 51, 234))
    
    # Background 27" 4K Monitor
    mcx, mcy = 640, 340
    draw.rounded_rectangle([mcx - 340, mcy - 200, mcx + 340, mcy + 180], radius=14, fill=(16, 20, 32, 255), outline=(0, 240, 255, 200), width=4)
    draw.rounded_rectangle([mcx - 325, mcy - 185, mcx + 325, mcy + 165], radius=8, fill=(8, 12, 22, 255))
    # Screen artwork (4K video editing interface timeline)
    draw.rectangle([mcx - 320, mcy + 80, mcx + 320, mcy + 155], fill=(22, 28, 44, 255))
    for tx in range(mcx - 300, mcx + 300, 90):
        draw.rounded_rectangle([tx, mcy + 90, tx + 75, mcy + 115], radius=4, fill=(0, 240, 255, 180))
        draw.rounded_rectangle([tx + 20, mcy + 122, tx + 85, mcy + 147], radius=4, fill=(147, 51, 234, 180))
        
    # Foreground Studio Laptop (open angle)
    lcx, lcy = 500, 600
    # Laptop screen
    draw.rounded_rectangle([lcx - 220, lcy - 150, lcx + 220, lcy + 20], radius=10, fill=(20, 25, 38, 255), outline=(255, 255, 255, 180), width=3)
    draw.rectangle([lcx - 210, lcy - 140, lcx + 210, lcy + 10], fill=(10, 14, 24, 255))
    # Laptop base / keyboard
    draw.polygon([(lcx - 250, lcy + 140), (lcx + 250, lcy + 140), (lcx + 220, lcy + 20), (lcx - 220, lcy + 20)], fill=(32, 38, 54, 255), outline=(0, 240, 255, 150), width=2)
    # Trackpad & Keyboard glow
    draw.rectangle([lcx - 180, lcy + 35, lcx + 180, lcy + 95], fill=(18, 22, 34, 255), outline=(0, 240, 255, 100), width=1)
    
    # External Portable SSD drive on right side
    scx, scy = 920, 640
    draw.rounded_rectangle([scx - 70, scy - 45, scx + 70, scy + 45], radius=12, fill=(40, 48, 66, 255), outline=(147, 51, 234, 220), width=3)
    draw.ellipse([scx - 45, scy - 12, scx - 25, scy + 12], fill=(0, 240, 255, 255))
    draw.text((scx - 10, scy - 10), "2TB SSD", fill=(255, 255, 255, 230))
    
    save_supersampled(img, filepath, 640, 480)

def gen_bundle_2(filepath):
    # Ultimate Gaming Rig Pack: RTX Gaming PC + 360Hz Display + Mech KB
    img, draw = create_studio_bg(1280, 960, (236, 72, 153), (0, 240, 255))
    
    # RTX Gaming PC Tower on left
    tcx, tcy = 380, 480
    draw.rounded_rectangle([tcx - 140, tcy - 300, tcx + 140, tcy + 300], radius=16, fill=(18, 22, 32, 255), outline=(236, 72, 153, 240), width=4)
    # Tempered glass panel with interior RGB fans
    draw.rounded_rectangle([tcx - 120, tcy - 270, tcx + 120, tcy + 270], radius=10, fill=(8, 12, 20, 255), outline=(255, 255, 255, 40), width=2)
    # 3 RGB fans inside
    for fy in [tcy - 170, tcy, tcy + 170]:
        draw.ellipse([tcx - 55, fy - 55, tcx + 55, fy + 55], outline=(0, 240, 255, 255), width=6)
        draw.ellipse([tcx - 20, fy - 20, tcx + 20, fy + 20], fill=(236, 72, 153, 255))
        
    # 360Hz Display on right
    mcx, mcy = 820, 400
    draw.rounded_rectangle([mcx - 260, mcy - 160, mcx + 260, mcy + 140], radius=12, fill=(15, 18, 28, 255), outline=(0, 240, 255, 220), width=4)
    draw.rectangle([mcx - 248, mcy - 148, mcx + 248, mcy + 128], fill=(6, 8, 16, 255))
    draw.text((mcx - 70, mcy - 10), "360Hz GAMING", fill=(0, 240, 255, 240))
    
    # RGB Mechanical Keyboard in front of display
    kcx, kcy = 820, 650
    draw.rounded_rectangle([kcx - 240, kcy - 40, kcx + 240, kcy + 40], radius=8, fill=(28, 34, 48, 255), outline=(236, 72, 153, 200), width=2)
    for kx in range(kcx - 220, kcx + 220, 25):
        draw.rectangle([kx, kcy - 30, kx + 18, kcy + 30], fill=(0, 240, 255, 120))
        
    save_supersampled(img, filepath, 640, 480)

def gen_bundle_3(filepath):
    # Mobile Power User Ecosystem: Flagship Phone + Wireless Buds + GaN Charger
    img, draw = create_studio_bg(1280, 960, (245, 158, 11), (59, 130, 246))
    
    # Flagship Smartphone in center
    pcx, pcy = 540, 480
    draw.rounded_rectangle([pcx - 130, pcy - 270, pcx + 130, pcy + 270], radius=32, fill=(18, 22, 34, 255), outline=(245, 158, 11, 240), width=5)
    draw.rounded_rectangle([pcx - 118, pcy - 258, pcx + 118, pcy + 258], radius=26, fill=(8, 10, 18, 255))
    draw.ellipse([pcx - 15, pcy - 245, pcx + 15, pcy - 215], fill=(245, 158, 11, 200))
    
    # Wireless Earbuds Charging Case on right
    bcx, bcy = 860, 440
    draw.rounded_rectangle([bcx - 90, bcy - 70, bcx + 90, bcy + 70], radius=28, fill=(30, 36, 52, 255), outline=(59, 130, 246, 220), width=3)
    draw.line([(bcx - 85, bcy), (bcx + 85, bcy)], fill=(245, 158, 11, 150), width=2)
    # Earbud stems popping up
    draw.rounded_rectangle([bcx - 45, bcy - 110, bcx - 15, bcy - 40], radius=10, fill=(255, 255, 255, 240))
    draw.rounded_rectangle([bcx + 15, bcy - 110, bcx + 45, bcy - 40], radius=10, fill=(255, 255, 255, 240))
    
    # GaN 100W Fast Charger block
    ccx, ccy = 860, 640
    draw.rounded_rectangle([ccx - 75, ccy - 60, ccx + 75, ccy + 60], radius=14, fill=(35, 42, 60, 255), outline=(245, 158, 11, 220), width=3)
    draw.rectangle([ccx - 50, ccy - 35, ccx - 20, ccy - 15], fill=(59, 130, 246, 255))
    draw.rectangle([ccx - 50, ccy + 15, ccx - 20, ccy + 35], fill=(59, 130, 246, 255))
    draw.text((ccx, ccy - 10), "100W GaN", fill=(255, 255, 255, 230))
    
    save_supersampled(img, filepath, 640, 480)

def gen_bundle_4(filepath):
    # Audio Enthusiast Studio Pair: Studio Headphones + USB Stream Mic
    img, draw = create_studio_bg(1280, 960, (16, 185, 129), (99, 102, 241))
    
    # Studio Headphones on left
    hcx, hcy = 460, 480
    # Headband arc
    draw.arc([hcx - 180, hcy - 260, hcx + 180, hcy + 40], start=180, end=360, fill=(99, 102, 241, 255), width=24)
    # Earcups
    draw.ellipse([hcx - 210, hcy - 80, hcx - 110, hcy + 120], fill=(26, 32, 46, 255), outline=(16, 185, 129, 240), width=6)
    draw.ellipse([hcx + 110, hcy - 80, hcx + 210, hcy + 120], fill=(26, 32, 46, 255), outline=(16, 185, 129, 240), width=6)
    
    # USB Stream Microphone on right
    mcx, mcy = 850, 480
    # Mic capsule
    draw.rounded_rectangle([mcx - 65, mcy - 180, mcx + 65, mcy + 60], radius=32, fill=(20, 26, 40, 255), outline=(99, 102, 241, 240), width=4)
    # Mesh grille lines
    for gy in range(mcy - 160, mcy - 20, 15):
        draw.line([(mcx - 55, gy), (mcx + 55, gy)], fill=(16, 185, 129, 180), width=2)
    # Desktop Stand base
    draw.ellipse([mcx - 90, mcy + 180, mcx + 90, mcy + 220], fill=(32, 38, 54, 255), outline=(99, 102, 241, 200), width=3)
    draw.rectangle([mcx - 12, mcy + 60, mcx + 12, mcy + 195], fill=(45, 52, 70, 255))
    
    save_supersampled(img, filepath, 640, 480)

# ----------------- DEAL CARDS (deal_1 to deal_6) -----------------

def gen_deal_card(filepath, cat_name, title_text, c1, c2):
    img, draw = create_studio_bg(1280, 960, c1, c2)
    cx, cy = 640, 480
    
    # Decorative glass backdrop card
    draw.rounded_rectangle([cx - 450, cy - 300, cx + 450, cy + 300], radius=24, fill=(15, 20, 32, 180), outline=(*c1, 220), width=4)
    
    # Glowing Badge tag
    draw.rounded_rectangle([cx - 410, cy - 260, cx - 210, cy - 200], radius=12, fill=(*c1, 230))
    draw.text((cx - 390, cy - 242), cat_name.upper(), fill=(10, 15, 28, 255))
    
    # Large Title Text
    draw.text((cx - 410, cy - 150), title_text, fill=(255, 255, 255, 255))
    
    # Abstract tech visual graphic
    draw.ellipse([cx + 100, cy - 120, cx + 380, cy + 160], outline=(*c2, 240), width=6)
    draw.polygon([(cx + 240, cy - 180), (cx + 380, cy + 80), (cx + 100, cy + 80)], outline=(*c1, 200), width=4)
    
    save_supersampled(img, filepath, 800, 600)

# ----------------- CLEARANCE CARDS (clearance_1 to clearance_4) -----------------

def gen_clearance_card(filepath, name, c1, c2):
    img, draw = create_studio_bg(1280, 960, c1, c2)
    cx, cy = 640, 480
    
    draw.rounded_rectangle([cx - 400, cy - 260, cx + 400, cy + 260], radius=20, fill=(14, 18, 28, 200), outline=(*c1, 200), width=4)
    draw.text((cx - 180, cy - 20), name, fill=(255, 255, 255, 240))
    
    save_supersampled(img, filepath, 640, 480)


def main():
    print("Generating all high-resolution CTA, Deal, Bundle, and Monitor assets...")
    
    # CTA Backgrounds
    gen_cta_bg("assets/images/home/bulk_cta_bg.png", "BULK ORDERS", (0, 240, 255), (59, 130, 246))
    gen_cta_bg("assets/images/home/newsletter_cta_bg.png", "NEWSLETTER", (147, 51, 234), (236, 72, 153))
    gen_cta_bg("assets/images/home/final_cta_bg.png", "FINAL CTA", (16, 185, 129), (0, 240, 255))
    gen_cta_bg("assets/images/home/home2_final_cta_bg.png", "SHOWROOM CTA", (245, 158, 11), (236, 72, 153))
    gen_cta_bg("assets/images/home/about_final_cta_bg.png", "ABOUT CTA", (99, 102, 241), (147, 51, 234))
    gen_cta_bg("assets/images/home/compare_cta_bg.png", "COMPARE CTA", (0, 240, 255), (16, 185, 129))
    gen_cta_bg("assets/images/home/contact_cta_bg.png", "CONTACT CTA", (99, 102, 241), (0, 240, 255))

    # Monitors
    gen_pixelview_27("assets/images/products/product_20.png")
    gen_rog_swift_360("assets/images/products/product_35.png")

    # Bundles
    gen_bundle_1("assets/images/deals/bundle_1.png")
    gen_bundle_2("assets/images/deals/bundle_2.png")
    gen_bundle_3("assets/images/deals/bundle_3.png")
    gen_bundle_4("assets/images/deals/bundle_4.png")

    # Deal Cards
    gen_deal_card("assets/images/deals/deal_1.png", "Flash Sale", "Up to 30% Off Laptops", (0, 240, 255), (147, 51, 234))
    gen_deal_card("assets/images/deals/deal_2.png", "Smartphone Event", "Extra $150 Trade-in Bonus", (245, 158, 11), (236, 72, 153))
    gen_deal_card("assets/images/deals/deal_3.png", "Audio Festival", "Headphones & Earbuds Specials", (16, 185, 129), (59, 130, 246))
    gen_deal_card("assets/images/deals/deal_4.png", "Gaming Bundle", "Free Keyboard with RTX Rigs", (236, 72, 153), (0, 240, 255))
    gen_deal_card("assets/images/deals/deal_5.png", "Fitness Upgrade", "Smartwatch Strap Packs", (59, 130, 246), (245, 158, 11))
    gen_deal_card("assets/images/deals/deal_6.png", "Clearance", "240Hz Monitors Up to $200 Off", (147, 51, 234), (16, 185, 129))

    # Clearance Cards
    gen_clearance_card("assets/images/deals/clearance_1.png", "PixelView 32 OLED", (0, 240, 255), (147, 51, 234))
    gen_clearance_card("assets/images/deals/clearance_2.png", "SoundHalo ANC", (236, 72, 153), (245, 158, 11))
    gen_clearance_card("assets/images/deals/clearance_3.png", "EliteBook 14 Demo", (16, 185, 129), (59, 130, 246))
    gen_clearance_card("assets/images/deals/clearance_4.png", "PulseWatch Fit Open-Box", (245, 158, 11), (0, 240, 255))

    print("All assets generated successfully!")

if __name__ == "__main__":
    main()
