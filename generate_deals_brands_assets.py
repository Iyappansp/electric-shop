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

def create_base_studio(width=1280, height=800, c1=(0, 240, 255), c2=(147, 51, 234), bg=(10, 14, 24)):
    img = Image.new("RGBA", (width, height), (*bg, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    
    draw_radial_gradient(gdraw, width, height, int(width * 0.3), int(height * 0.4), int(min(width, height) * 0.7), (*c1, 120), (*bg, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.7), int(height * 0.6), int(min(width, height) * 0.7), (*c2, 110), (*bg, 0))
    
    glow = glow.filter(ImageFilter.GaussianBlur(radius=50))
    img.alpha_composite(glow)
    
    # Grid lines
    draw = ImageDraw.Draw(img)
    step = 60
    for x in range(0, width, step):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, step):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)
        
    return img

def save_img(img, filepath, w=800, h=500):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    resized = img.resize((w, h), Image.Resampling.LANCZOS)
    resized.save(filepath, "PNG", quality=95)
    print(f"Saved: {filepath}")

# --- DEALS 1 to 6 ---
def gen_deal_1(fp):
    img = create_base_studio(1280, 800, (59, 130, 246), (245, 158, 11))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 400
    draw.polygon([(cx-260, cy-160), (cx+260, cy-160), (cx+290, cy+60), (cx-290, cy+60)], fill=(15, 23, 42, 255), outline=(59, 130, 246, 240), width=4)
    draw.polygon([(cx-240, cy-140), (cx+240, cy-140), (cx+270, cy+40), (cx-270, cy+40)], fill=(8, 12, 24, 255), outline=(245, 158, 11, 200), width=2)
    draw.polygon([(cx-290, cy+60), (cx+290, cy+60), (cx+340, cy+180), (cx-340, cy+180)], fill=(30, 41, 59, 255), outline=(59, 130, 246, 200), width=3)
    save_img(img, fp)

def gen_deal_2(fp):
    img = create_base_studio(1280, 800, (147, 51, 234), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 400
    w, h = 160, 300
    draw.rounded_rectangle([cx-w, cy-h, cx+w, cy+h], radius=36, fill=(18, 24, 38, 255), outline=(147, 51, 234, 240), width=6)
    draw.rounded_rectangle([cx-w+15, cy-h+20, cx+w-15, cy+h-20], radius=24, fill=(6, 12, 26, 255), outline=(0, 240, 255, 180), width=3)
    draw.ellipse([cx-80, cy-220, cx+80, cy-60], fill=(30, 41, 59, 255), outline=(147, 51, 234, 200), width=3)
    save_img(img, fp)

def gen_deal_3(fp):
    img = create_base_studio(1280, 800, (236, 72, 153), (245, 158, 11))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.arc([cx-220, cy-220, cx+220, cy+180], start=190, end=350, fill=(236, 72, 153, 255), width=18)
    draw.ellipse([cx-260, cy-20, cx-160, cy+160], fill=(24, 30, 48, 255), outline=(245, 158, 11, 240), width=6)
    draw.ellipse([cx+160, cy-20, cx+260, cy+160], fill=(24, 30, 48, 255), outline=(245, 158, 11, 240), width=6)
    save_img(img, fp)

def gen_deal_4(fp):
    img = create_base_studio(1280, 800, (16, 185, 129), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 520, 380
    draw.rounded_rectangle([cx-140, cy-220, cx+140, cy+220], radius=24, fill=(15, 23, 42, 255), outline=(0, 240, 255, 240), width=6)
    draw.ellipse([cx-60, cy-120, cx+60, cy], fill=(16, 185, 129, 60), outline=(16, 185, 129, 255), width=4)
    draw.ellipse([cx-60, cy+20, cx+60, cy+140], fill=(0, 240, 255, 60), outline=(0, 240, 255, 255), width=4)
    draw.polygon([(cx+160, cy+80), (cx+420, cy+80), (cx+460, cy+200), (cx+180, cy+200)], fill=(30, 41, 59, 255), outline=(16, 185, 129, 220), width=4)
    save_img(img, fp)

def gen_deal_5(fp):
    img = create_base_studio(1280, 800, (245, 158, 11), (236, 72, 153))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 400
    draw.rounded_rectangle([cx-140, cy-140, cx+140, cy+140], radius=40, fill=(30, 41, 59, 255), outline=(245, 158, 11, 240), width=6)
    draw.ellipse([cx-110, cy-110, cx+110, cy+110], fill=(15, 23, 42, 255), outline=(236, 72, 153, 200), width=3)
    draw.rounded_rectangle([cx-320, cy-180, cx-240, cy+180], radius=20, fill=(236, 72, 153, 200), outline=(255, 255, 255, 80), width=2)
    draw.rounded_rectangle([cx+240, cy-180, cx+320, cy+180], radius=20, fill=(0, 240, 255, 200), outline=(255, 255, 255, 80), width=2)
    save_img(img, fp)

def gen_deal_6(fp):
    img = create_base_studio(1280, 800, (0, 240, 255), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 360
    pts = [(cx-340, cy-140), (cx+340, cy-140), (cx+320, cy+120), (cx-320, cy+120)]
    draw.polygon(pts, fill=(15, 23, 42, 255), outline=(0, 240, 255, 240), width=6)
    draw.polygon([(cx-40, cy+120), (cx+40, cy+120), (cx+80, cy+220), (cx-80, cy+220)], fill=(30, 41, 59, 255), outline=(147, 51, 234, 200), width=3)
    save_img(img, fp)

# --- BUNDLES 1 to 4 ---
def gen_bundle_1(fp):
    img = create_base_studio(1280, 800, (59, 130, 246), (16, 185, 129))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.rounded_rectangle([cx-220, cy-180, cx+220, cy+60], radius=16, fill=(15, 23, 42, 255), outline=(59, 130, 246, 240), width=4)
    draw.polygon([(cx-180, cy), (cx+180, cy), (cx+220, cy+160), (cx-220, cy+160)], fill=(30, 41, 59, 255), outline=(16, 185, 129, 220), width=3)
    save_img(img, fp, 640, 480)

def gen_bundle_2(fp):
    img = create_base_studio(1280, 800, (236, 72, 153), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.rounded_rectangle([cx-300, cy-140, cx-120, cy+160], radius=20, fill=(15, 23, 42, 255), outline=(236, 72, 153, 240), width=4)
    draw.rounded_rectangle([cx-80, cy-180, cx+280, cy+60], radius=16, fill=(15, 23, 42, 255), outline=(0, 240, 255, 240), width=4)
    draw.ellipse([cx+120, cy+80, cx+220, cy+180], fill=(30, 41, 59, 255), outline=(236, 72, 153, 200), width=3)
    save_img(img, fp, 640, 480)

def gen_bundle_3(fp):
    img = create_base_studio(1280, 800, (245, 158, 11), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.rounded_rectangle([cx-180, cy-160, cx-60, cy+160], radius=28, fill=(15, 23, 42, 255), outline=(245, 158, 11, 240), width=4)
    draw.rounded_rectangle([cx, cy-40, cx+140, cy+120], radius=30, fill=(30, 41, 59, 255), outline=(147, 51, 234, 220), width=3)
    draw.rounded_rectangle([cx+160, cy-120, cx+260, cy+20], radius=16, fill=(24, 30, 48, 255), outline=(245, 158, 11, 200), width=3)
    save_img(img, fp, 640, 480)

def gen_bundle_4(fp):
    img = create_base_studio(1280, 800, (0, 240, 255), (236, 72, 153))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.arc([cx-220, cy-180, cx, cy+140], start=190, end=350, fill=(0, 240, 255, 255), width=14)
    draw.rounded_rectangle([cx+60, cy-160, cx+180, cy+100], radius=40, fill=(30, 41, 59, 255), outline=(236, 72, 153, 240), width=4)
    save_img(img, fp, 640, 480)

# --- CLEARANCE 1 to 4 ---
def gen_clearance_1(fp):
    img = create_base_studio(1280, 800, (239, 68, 68), (245, 158, 11))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.rounded_rectangle([cx-240, cy-160, cx+240, cy+100], radius=20, fill=(15, 23, 42, 255), outline=(239, 68, 68, 240), width=5)
    save_img(img, fp, 640, 480)

def gen_clearance_2(fp):
    img = create_base_studio(1280, 800, (239, 68, 68), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.ellipse([cx-140, cy-140, cx+140, cy+140], fill=(24, 30, 48, 255), outline=(239, 68, 68, 240), width=6)
    save_img(img, fp, 640, 480)

def gen_clearance_3(fp):
    img = create_base_studio(1280, 800, (239, 68, 68), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.polygon([(cx-220, cy-120), (cx+220, cy-120), (cx+260, cy+100), (cx-260, cy+100)], fill=(15, 23, 42, 255), outline=(239, 68, 68, 240), width=4)
    save_img(img, fp, 640, 480)

def gen_clearance_4(fp):
    img = create_base_studio(1280, 800, (239, 68, 68), (16, 185, 129))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 380
    draw.rounded_rectangle([cx-120, cy-140, cx+120, cy+140], radius=36, fill=(30, 41, 59, 255), outline=(239, 68, 68, 240), width=5)
    save_img(img, fp, 640, 480)

# --- BRAND SPOTLIGHT BANNERS ---
def gen_brand_rog_spotlight(fp):
    img = create_base_studio(1280, 600, (239, 68, 68), (147, 51, 234), bg=(8, 10, 18))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 900, 300
    draw.polygon([(cx-260, cy-180), (cx+260, cy-180), (cx+300, cy+80), (cx-300, cy+80)], fill=(15, 20, 32, 255), outline=(239, 68, 68, 255), width=5)
    draw.polygon([(cx-300, cy+80), (cx+300, cy+80), (cx+360, cy+200), (cx-360, cy+200)], fill=(24, 30, 48, 255), outline=(147, 51, 234, 220), width=4)
    draw.polygon([(cx-80, cy-80), (cx+80, cy-80), (cx, cy+40)], fill=(239, 68, 68, 180))
    save_img(img, fp, 1280, 480)

def gen_brand_apple_spotlight(fp):
    img = create_base_studio(1280, 600, (255, 255, 255), (59, 130, 246), bg=(12, 16, 26))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 900, 300
    draw.rounded_rectangle([cx-320, cy-180, cx+160, cy+120], radius=24, fill=(20, 28, 44, 240), outline=(255, 255, 255, 120), width=3)
    draw.rounded_rectangle([cx+80, cy-120, cx+220, cy+180], radius=32, fill=(15, 22, 36, 255), outline=(59, 130, 246, 200), width=4)
    draw.ellipse([cx-220, cy+40, cx-80, cy+180], fill=(28, 36, 54, 255), outline=(255, 255, 255, 180), width=3)
    save_img(img, fp, 1280, 480)

if __name__ == "__main__":
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    deals_dir = os.path.join(base_dir, "deals")
    brands_dir = os.path.join(base_dir, "brands")
    
    gen_deal_1(os.path.join(deals_dir, "deal_1.png"))
    gen_deal_2(os.path.join(deals_dir, "deal_2.png"))
    gen_deal_3(os.path.join(deals_dir, "deal_3.png"))
    gen_deal_4(os.path.join(deals_dir, "deal_4.png"))
    gen_deal_5(os.path.join(deals_dir, "deal_5.png"))
    gen_deal_6(os.path.join(deals_dir, "deal_6.png"))
    
    gen_bundle_1(os.path.join(deals_dir, "bundle_1.png"))
    gen_bundle_2(os.path.join(deals_dir, "bundle_2.png"))
    gen_bundle_3(os.path.join(deals_dir, "bundle_3.png"))
    gen_bundle_4(os.path.join(deals_dir, "bundle_4.png"))
    
    gen_clearance_1(os.path.join(deals_dir, "clearance_1.png"))
    gen_clearance_2(os.path.join(deals_dir, "clearance_2.png"))
    gen_clearance_3(os.path.join(deals_dir, "clearance_3.png"))
    gen_clearance_4(os.path.join(deals_dir, "clearance_4.png"))
    
    gen_brand_rog_spotlight(os.path.join(brands_dir, "brand_rog_spotlight.png"))
    gen_brand_apple_spotlight(os.path.join(brands_dir, "brand_apple_spotlight.png"))
    print("All image generation complete!")
