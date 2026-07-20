import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def draw_radial_gradient(draw, width, height, center_x, center_y, radius, color_center, color_outer):
    for r in range(radius, 0, -3):
        t = r / radius
        r_col = int(color_center[0] * (1 - t) + color_outer[0] * t)
        g_col = int(color_center[1] * (1 - t) + color_outer[1] * t)
        b_col = int(color_center[2] * (1 - t) + color_outer[2] * t)
        a_col = int(color_center[3] * (1 - t) + color_outer[3] * t) if len(color_center) > 3 else 255
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(r_col, g_col, b_col, a_col))

def create_base_studio_hi_res(width=1280, height=960, accent_color_1=(0, 240, 255), accent_color_2=(138, 43, 226)):
    # Dark studio background (supersampled)
    img = Image.new("RGBA", (width, height), (8, 12, 20, 255))
    glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow_layer)
    
    # Dual neon ambient spotlights
    draw_radial_gradient(gdraw, width, height, int(width * 0.35), int(height * 0.38), int(min(width, height) * 0.65), (*accent_color_1, 110), (8, 12, 20, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.65), int(height * 0.62), int(min(width, height) * 0.70), (*accent_color_2, 100), (8, 12, 20, 0))
    
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=60))
    img.alpha_composite(glow_layer)
    
    # Soft tech grid lines
    grid_draw = ImageDraw.Draw(img)
    grid_step = 80
    for x in range(0, width, grid_step):
        grid_draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 10), width=1)
    for y in range(0, height, grid_step):
        grid_draw.line([(0, y), (width, y)], fill=(255, 255, 255, 10), width=1)
        
    return img

def save_supersampled(img, filepath, target_w=640, target_h=480):
    img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    img_resized.save(filepath, "PNG", quality=95)
    print(f"Generated high-quality asset: {filepath}")

# 1. ChronoLux Premium (ID 16) - Gold/Rose luxury smartwatch
def gen_chronolux_premium(filepath):
    img = create_base_studio_hi_res(1280, 960, (245, 158, 11), (236, 72, 153))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    
    # Metal link strap
    draw.rounded_rectangle([cx - 90, cy - 380, cx + 90, cy + 380], radius=24, fill=(35, 30, 40, 240), outline=(245, 158, 11, 220), width=4)
    for y_link in range(cy - 360, cy + 360, 40):
        if abs(y_link - cy) > 140:
            draw.line([(cx - 85, y_link), (cx + 85, y_link)], fill=(245, 158, 11, 100), width=2)

    # Gold ceramic bezel
    r = 200
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(22, 20, 28, 255), outline=(245, 158, 11, 255), width=8)
    draw.ellipse([cx - int(r*0.92), cy - int(r*0.92), cx + int(r*0.92), cy + int(r*0.92)], fill=(12, 10, 18, 255), outline=(255, 255, 255, 40), width=2)
    
    # Chronograph sub-dials & watch face hands
    draw.ellipse([cx - 70, cy - 90, cx - 10, cy - 30], fill=(20, 18, 30, 255), outline=(236, 72, 153, 200), width=2)
    draw.ellipse([cx + 10, cy - 90, cx + 70, cy - 30], fill=(20, 18, 30, 255), outline=(0, 240, 255, 200), width=2)
    draw.ellipse([cx - 30, cy + 30, cx + 30, cy + 90], fill=(20, 18, 30, 255), outline=(245, 158, 11, 200), width=2)
    
    # Watch hands
    draw.line([(cx, cy), (cx + 60, cy - 60)], fill=(245, 158, 11, 255), width=5)
    draw.line([(cx, cy), (cx - 40, cy + 80)], fill=(255, 255, 255, 255), width=4)
    draw.circle((cx, cy), radius=10, fill=(245, 158, 11, 255))
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "CHRONOLUX PREMIUM", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 2. Apex Run Ultra (ID 36) - Rugged titanium fitness watch
def gen_apex_run_ultra(filepath):
    img = create_base_studio_hi_res(1280, 960, (0, 240, 255), (16, 185, 129))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    
    # Orange ribbed sport band
    draw.rounded_rectangle([cx - 85, cy - 380, cx + 85, cy + 380], radius=20, fill=(234, 88, 12, 230), outline=(255, 255, 255, 80), width=3)
    for y_rib in range(cy - 360, cy + 360, 30):
        if abs(y_rib - cy) > 150:
            draw.line([(cx - 75, y_rib), (cx + 75, y_rib)], fill=(194, 65, 12, 255), width=4)

    # Squircle Titanium Case
    w, h = 190, 210
    draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=60, fill=(28, 36, 48, 255), outline=(0, 240, 255, 240), width=8)
    
    # Orange Action Button on side
    draw.rounded_rectangle([cx - w - 20, cy - 40, cx - w, cy + 40], radius=8, fill=(249, 115, 22, 255))
    
    # OLED Display area
    draw.rounded_rectangle([cx - int(w*0.82), cy - int(h*0.84), cx + int(w*0.82), cy + int(h*0.84)], radius=40, fill=(6, 12, 22, 255), outline=(16, 185, 129, 200), width=3)
    
    # Fitness metric arcs
    draw.arc([cx - 120, cy - 120, cx + 120, cy + 120], start=30, end=300, fill=(0, 240, 255, 255), width=10)
    draw.arc([cx - 95, cy - 95, cx + 95, cy + 95], start=100, end=340, fill=(16, 185, 129, 255), width=8)
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "APEX RUN ULTRA", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 3. Galaxy Watch Ultra 2 (ID 37) - Premium violet/cyan dark watch
def gen_galaxy_watch_ultra(filepath):
    img = create_base_studio_hi_res(1280, 960, (147, 51, 234), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    
    # Dark silicone strap
    draw.rounded_rectangle([cx - 80, cy - 380, cx + 80, cy + 380], radius=18, fill=(18, 24, 38, 240), outline=(147, 51, 234, 200), width=3)
    
    # Circular watch face inside square titanium body
    draw.rounded_rectangle([cx - 190, cy - 190, cx + 190, cy + 190], radius=50, fill=(24, 30, 44, 255), outline=(147, 51, 234, 240), width=6)
    draw.ellipse([cx - 165, cy - 165, cx + 165, cy + 165], fill=(8, 14, 26, 255), outline=(0, 240, 255, 220), width=4)
    
    # Glowing digital watch display
    draw.arc([cx - 130, cy - 130, cx + 130, cy + 130], start=45, end=270, fill=(147, 51, 234, 255), width=8)
    draw.arc([cx - 105, cy - 105, cx + 105, cy + 105], start=120, end=350, fill=(0, 240, 255, 255), width=6)
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "GALAXY WATCH ULTRA 2", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 4. AirWave Buds 2 (ID 14) - Glossy wireless earbud case
def gen_airwave_buds(filepath):
    img = create_base_studio_hi_res(1280, 960, (236, 72, 153), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    
    # Charging case (glossy white/dark metallic)
    draw.rounded_rectangle([cx - 170, cy - 80, cx + 170, cy + 160], radius=70, fill=(18, 26, 42, 240), outline=(236, 72, 153, 220), width=6)
    draw.line([(cx - 165, cy + 20), (cx + 165, cy + 20)], fill=(0, 240, 255, 160), width=3)
    
    # Status LED indicator
    draw.circle((cx, cy + 90), radius=10, fill=(0, 240, 255, 255))
    
    # Earbuds standing out top
    # Left Earbud
    draw.ellipse([cx - 110, cy - 200, cx - 30, cy - 100], fill=(28, 38, 58, 255), outline=(236, 72, 153, 240), width=4)
    draw.rounded_rectangle([cx - 80, cy - 120, cx - 60, cy - 30], radius=10, fill=(28, 38, 58, 255), outline=(0, 240, 255, 200), width=3)
    
    # Right Earbud
    draw.ellipse([cx + 30, cy - 200, cx + 110, cy - 100], fill=(28, 38, 58, 255), outline=(236, 72, 153, 240), width=4)
    draw.rounded_rectangle([cx + 60, cy - 120, cx + 80, cy - 30], radius=10, fill=(28, 38, 58, 255), outline=(0, 240, 255, 200), width=3)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "AIRWAVE BUDS 2", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 5. TitanForce Gaming PC (ID 19) - Desktop tower PC with RGB fans
def gen_titanforce_pc(filepath):
    img = create_base_studio_hi_res(1280, 960, (236, 72, 153), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 430
    w, h = 210, 320
    
    # Main Tower Chassis
    draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=24, fill=(14, 20, 32, 255), outline=(0, 240, 255, 240), width=6)
    
    # Tempered glass side panel
    draw.rounded_rectangle([cx - int(w*0.82), cy - int(h*0.84), cx + int(w*0.82), cy + int(h*0.84)], radius=16, fill=(6, 12, 22, 240), outline=(236, 72, 153, 180), width=4)
    
    # Internal components & RGB Dual Fans
    draw.ellipse([cx - 90, cy - 180, cx + 90, cy - 20], fill=(12, 20, 36, 255), outline=(0, 240, 255, 255), width=6)
    draw.ellipse([cx - 90, cy + 20, cx + 90, cy + 180], fill=(12, 20, 36, 255), outline=(236, 72, 153, 255), width=6)
    
    # Liquid CPU Cooler Block
    draw.rounded_rectangle([cx - 45, cy - 60, cx + 45, cy + 20], radius=12, fill=(20, 28, 48, 255), outline=(255, 255, 255, 140), width=3)
    draw.circle((cx, cy - 20), radius=15, fill=(0, 240, 255, 255))
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "TITANFORCE GAMING PC", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 6. StreamCast Capture (ID 22) - Metal HDMI capture box
def gen_streamcast_capture(filepath):
    img = create_base_studio_hi_res(1280, 960, (0, 240, 255), (236, 72, 153))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    w, h = 260, 140
    
    # Metal enclosure box
    draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=24, fill=(18, 24, 38, 255), outline=(0, 240, 255, 240), width=6)
    
    # Glossy top panel strip
    draw.rounded_rectangle([cx - int(w*0.85), cy - int(h*0.5), cx + int(w*0.85), cy + int(h*0.5)], radius=12, fill=(8, 14, 26, 255), outline=(236, 72, 153, 180), width=3)
    
    # Status LED indicator lights
    draw.circle((cx - 120, cy), radius=16, fill=(0, 240, 255, 255))
    draw.circle((cx, cy), radius=16, fill=(236, 72, 153, 255))
    draw.circle((cx + 120, cy), radius=16, fill=(16, 185, 129, 255))
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "STREAMCAST CAPTURE", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 7. Pulse Lite 5G (ID 8) - Ultra-slim 5G smartphone
def gen_pulse_lite_5g(filepath):
    img = create_base_studio_hi_res(1280, 960, (16, 185, 129), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 430
    w, h = 180, 340
    
    # Phone body chassis
    draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=40, fill=(14, 22, 36, 255), outline=(16, 185, 129, 240), width=6)
    
    # Screen area
    draw.rounded_rectangle([cx - int(w*0.9), cy - int(h*0.94), cx + int(w*0.9), cy + int(h*0.94)], radius=30, fill=(4, 10, 22, 255), outline=(0, 240, 255, 160), width=2)
    
    # Camera hole-punch
    draw.circle((cx, cy - int(h*0.88)), radius=10, fill=(0, 0, 0, 255))
    
    # Dynamic abstract screen wallpaper curves
    draw.ellipse([cx - 120, cy - 180, cx + 120, cy + 180], outline=(16, 185, 129, 220), width=6)
    draw.ellipse([cx - 80, cy - 120, cx + 80, cy + 120], outline=(0, 240, 255, 200), width=4)
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "PULSE LITE 5G", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 8. Vortex Gaming Laptop RTX (ID 2) - RGB Gaming laptop
def gen_vortex_gaming_laptop(filepath):
    img = create_base_studio_hi_res(1280, 960, (147, 51, 234), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    w, h = 340, 190
    
    # Laptop Screen lid
    pts_s = [(cx - w, cy - h), (cx + w, cy - h), (cx + int(w*1.12), cy + int(h*0.2)), (cx - int(w*1.12), cy + int(h*0.2))]
    draw.polygon(pts_s, fill=(16, 22, 38, 255), outline=(147, 51, 234, 240), width=4)
    
    # Screen display
    disp_s = [(cx - int(w*0.92), cy - int(h*0.88)), (cx + int(w*0.92), cy - int(h*0.88)), (cx + int(w*1.02), cy + int(h*0.1)), (cx - int(w*1.02), cy + int(h*0.1))]
    draw.polygon(disp_s, fill=(6, 12, 26, 255), outline=(0, 240, 255, 200), width=3)
    
    # Laptop Deck
    pts_d = [(cx - int(w*1.12), cy + int(h*0.2)), (cx + int(w*1.12), cy + int(h*0.2)), (cx + int(w*1.3), cy + int(h*0.65)), (cx - int(w*1.3), cy + int(h*0.65))]
    draw.polygon(pts_d, fill=(22, 28, 46, 255), outline=(147, 51, 234, 220), width=4)
    
    # RGB Keyboard grid
    kb_pts = [(cx - int(w*0.95), cy + int(h*0.25)), (cx + int(w*0.95), cy + int(h*0.25)), (cx + int(w*1.15), cy + int(h*0.55)), (cx - int(w*1.15), cy + int(h*0.55))]
    draw.polygon(kb_pts, fill=(30, 38, 58, 240), outline=(236, 72, 153, 200), width=2)
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "VORTEX GAMING LAPTOP RTX", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

# 9. ThinkBook Studio 14 (ID 29) - Ultrathin creator studio laptop
def gen_thinkbook_studio(filepath):
    img = create_base_studio_hi_res(1280, 960, (59, 130, 246), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 440
    w, h = 330, 185
    
    # Screen
    pts_s = [(cx - w, cy - h), (cx + w, cy - h), (cx + int(w*1.08), cy + int(h*0.2)), (cx - int(w*1.08), cy + int(h*0.2))]
    draw.polygon(pts_s, fill=(18, 24, 38, 255), outline=(59, 130, 246, 240), width=4)
    
    disp_s = [(cx - int(w*0.92), cy - int(h*0.88)), (cx + int(w*0.92), cy - int(h*0.88)), (cx + int(w*1.0), cy + int(h*0.1)), (cx - int(w*1.0), cy + int(h*0.1))]
    draw.polygon(disp_s, fill=(8, 14, 28, 255), outline=(147, 51, 234, 180), width=2)
    
    # Deck
    pts_d = [(cx - int(w*1.08), cy + int(h*0.2)), (cx + int(w*1.08), cy + int(h*0.2)), (cx + int(w*1.24), cy + int(h*0.6)), (cx - int(w*1.24), cy + int(h*0.6))]
    draw.polygon(pts_d, fill=(24, 30, 48, 255), outline=(59, 130, 246, 200), width=3)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((cx, 880), "THINKBOOK STUDIO 14", fill=(255, 255, 255, 240), font=font, anchor="mm")
    except:
        pass
    save_supersampled(img, filepath)

if __name__ == "__main__":
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    prod_dir = os.path.join(base_dir, "products")
    
    gen_chronolux_premium(os.path.join(prod_dir, "product_16.png"))
    gen_apex_run_ultra(os.path.join(prod_dir, "product_36.png"))
    gen_galaxy_watch_ultra(os.path.join(prod_dir, "product_37.png"))
    gen_airwave_buds(os.path.join(prod_dir, "product_14.png"))
    gen_titanforce_pc(os.path.join(prod_dir, "product_19.png"))
    gen_streamcast_capture(os.path.join(prod_dir, "product_22.png"))
    gen_pulse_lite_5g(os.path.join(prod_dir, "product_8.png"))
    gen_vortex_gaming_laptop(os.path.join(prod_dir, "product_2.png"))
    gen_thinkbook_studio(os.path.join(prod_dir, "product_29.png"))
