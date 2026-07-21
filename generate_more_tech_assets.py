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

def create_studio(width=1280, height=800, c1=(0, 240, 255), c2=(147, 51, 234), bg=(12, 16, 26)):
    img = Image.new("RGBA", (width, height), (*bg, 255))
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    draw_radial_gradient(gdraw, width, height, int(width * 0.35), int(height * 0.4), int(min(width, height) * 0.65), (*c1, 110), (*bg, 0))
    draw_radial_gradient(gdraw, width, height, int(width * 0.65), int(height * 0.6), int(min(width, height) * 0.65), (*c2, 100), (*bg, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=45))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)
    return img

def save_img(img, filepath, w=640, h=480):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.resize((w, h), Image.Resampling.LANCZOS).save(filepath, "PNG", quality=95)
    print(f"Generated: {filepath}")

# 1. Team member 4 (Noah Kim) portrait
def gen_team_4(fp):
    img = create_studio(600, 600, (59, 130, 246), (16, 185, 129), bg=(18, 24, 38))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 300, 300
    # Head & shoulders avatar silhouette studio icon
    draw.ellipse([cx-100, cy-120, cx+100, cy+80], fill=(30, 41, 59, 255), outline=(59, 130, 246, 240), width=4)
    draw.ellipse([cx-70, cy-100, cx+70, cy+40], fill=(15, 23, 42, 255))
    draw.ellipse([cx-150, cy+100, cx+150, cy+320], fill=(30, 41, 59, 255), outline=(16, 185, 129, 200), width=4)
    save_img(img, fp, 300, 300)

# 2. Comparison images compare_1 to compare_4
def gen_compare_1(fp):
    # Laptop spec comparison
    img = create_studio(800, 600, (0, 240, 255), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 400, 300
    draw.polygon([(cx-200, cy-120), (cx+200, cy-120), (cx+220, cy+40), (cx-220, cy+40)], fill=(15, 23, 42, 255), outline=(0, 240, 255, 240), width=4)
    draw.polygon([(cx-220, cy+40), (cx+220, cy+40), (cx+260, cy+140), (cx-260, cy+140)], fill=(30, 41, 59, 255), outline=(147, 51, 234, 200), width=3)
    save_img(img, fp, 400, 300)

def gen_compare_2(fp):
    # Phone spec comparison
    img = create_studio(800, 600, (236, 72, 153), (245, 158, 11))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 400, 300
    draw.rounded_rectangle([cx-110, cy-200, cx+110, cy+200], radius=32, fill=(18, 24, 38, 255), outline=(236, 72, 153, 240), width=5)
    draw.ellipse([cx-50, cy-150, cx+50, cy-50], fill=(30, 41, 59, 255), outline=(245, 158, 11, 200), width=3)
    save_img(img, fp, 400, 300)

def gen_compare_3(fp):
    # Headphones spec comparison
    img = create_studio(800, 600, (16, 185, 129), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 400, 300
    draw.arc([cx-160, cy-160, cx+160, cy+140], start=190, end=350, fill=(16, 185, 129, 255), width=16)
    draw.ellipse([cx-180, cy-20, cx-100, cy+140], fill=(24, 30, 48, 255), outline=(0, 240, 255, 240), width=5)
    draw.ellipse([cx+100, cy-20, cx+180, cy+140], fill=(24, 30, 48, 255), outline=(0, 240, 255, 240), width=5)
    save_img(img, fp, 400, 300)

def gen_compare_4(fp):
    # Smartwatch spec comparison
    img = create_studio(800, 600, (245, 158, 11), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 400, 300
    draw.rounded_rectangle([cx-100, cy-100, cx+100, cy+100], radius=32, fill=(30, 41, 59, 255), outline=(245, 158, 11, 240), width=5)
    draw.ellipse([cx-80, cy-80, cx+80, cy+80], fill=(15, 23, 42, 255), outline=(147, 51, 234, 200), width=3)
    save_img(img, fp, 400, 300)

# 3. Dedicated ROG product images
def gen_rog_prod_1(fp):
    # AeroBook Pro 16 ROG edition
    img = create_studio(1280, 960, (239, 68, 68), (147, 51, 234))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.polygon([(cx-320, cy-220), (cx+320, cy-220), (cx+360, cy+60), (cx-360, cy+60)], fill=(12, 16, 28, 255), outline=(239, 68, 68, 255), width=5)
    draw.polygon([(cx-360, cy+60), (cx+360, cy+60), (cx+420, cy+220), (cx-420, cy+220)], fill=(24, 30, 48, 255), outline=(147, 51, 234, 220), width=4)
    save_img(img, fp)

def gen_rog_prod_2(fp):
    # Vortex Gaming Laptop ROG
    img = create_studio(1280, 960, (239, 68, 68), (0, 240, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.polygon([(cx-340, cy-240), (cx+340, cy-240), (cx+380, cy+40), (cx-380, cy+40)], fill=(8, 12, 22, 255), outline=(0, 240, 255, 240), width=5)
    draw.polygon([(cx-380, cy+40), (cx+380, cy+40), (cx+440, cy+240), (cx-440, cy+240)], fill=(28, 36, 54, 255), outline=(239, 68, 68, 240), width=4)
    save_img(img, fp)

def gen_rog_prod_3(fp):
    # Zenith Ultrabook X ROG
    img = create_studio(1280, 960, (147, 51, 234), (239, 68, 68))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.polygon([(cx-300, cy-200), (cx+300, cy-200), (cx+340, cy+80), (cx-340, cy+80)], fill=(16, 22, 36, 255), outline=(147, 51, 234, 240), width=5)
    draw.polygon([(cx-340, cy+80), (cx+340, cy+80), (cx+400, cy+220), (cx-400, cy+220)], fill=(24, 30, 48, 255), outline=(239, 68, 68, 200), width=4)
    save_img(img, fp)

def gen_rog_prod_4(fp):
    # TitanForce Gaming PC ROG
    img = create_studio(1280, 960, (239, 68, 68), (16, 185, 129))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-220, cy-320, cx+220, cy+320], radius=32, fill=(12, 16, 28, 255), outline=(239, 68, 68, 255), width=6)
    draw.ellipse([cx-100, cy-180, cx+100, cy+20], fill=(16, 185, 129, 80), outline=(16, 185, 129, 255), width=4)
    draw.ellipse([cx-100, cy+40, cx+100, cy+240], fill=(239, 68, 68, 80), outline=(239, 68, 68, 255), width=4)
    save_img(img, fp)

# 4. Dedicated Apple product images
def gen_apple_prod_1(fp):
    # AuraPhone Pro Max
    img = create_studio(1280, 960, (255, 255, 255), (59, 130, 246), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-180, cy-340, cx+180, cy+340], radius=44, fill=(18, 24, 38, 255), outline=(255, 255, 255, 200), width=6)
    save_img(img, fp)

def gen_apple_prod_2(fp):
    # AirWave Buds 2
    img = create_studio(1280, 960, (59, 130, 246), (236, 72, 153), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-180, cy-100, cx+180, cy+180], radius=70, fill=(24, 32, 48, 255), outline=(59, 130, 246, 240), width=6)
    save_img(img, fp)

def gen_apple_prod_3(fp):
    # ChronoLux Premium
    img = create_studio(1280, 960, (245, 158, 11), (255, 255, 255), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.ellipse([cx-180, cy-180, cx+180, cy+180], fill=(20, 26, 40, 255), outline=(245, 158, 11, 255), width=8)
    save_img(img, fp)

def gen_apple_prod_4(fp):
    # PowerLine 100W GaN Charger
    img = create_studio(1280, 960, (255, 255, 255), (147, 51, 234), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-160, cy-160, cx+160, cy+160], radius=32, fill=(28, 36, 54, 255), outline=(255, 255, 255, 220), width=5)
    save_img(img, fp)

def gen_apple_prod_5(fp):
    # iPhone 16 Pro
    img = create_studio(1280, 960, (59, 130, 246), (16, 185, 129), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-190, cy-350, cx+190, cy+350], radius=48, fill=(16, 22, 36, 255), outline=(59, 130, 246, 240), width=6)
    save_img(img, fp)

def gen_apple_prod_6(fp):
    # Apex Run Ultra Watch
    img = create_studio(1280, 960, (245, 158, 11), (239, 68, 68), bg=(10, 14, 24))
    draw = ImageDraw.Draw(img, "RGBA")
    cx, cy = 640, 480
    draw.rounded_rectangle([cx-190, cy-210, cx+190, cy+210], radius=54, fill=(28, 36, 52, 255), outline=(245, 158, 11, 240), width=7)
    save_img(img, fp)

if __name__ == "__main__":
    base_dir = r"c:\Users\infot\Contacts\OneDrive\Desktop\PDI\electric-shop\assets\images"
    
    gen_team_4(os.path.join(base_dir, "home", "team_4.png"))
    
    cat_dir = os.path.join(base_dir, "categories")
    gen_compare_1(os.path.join(cat_dir, "compare_1.png"))
    gen_compare_2(os.path.join(cat_dir, "compare_2.png"))
    gen_compare_3(os.path.join(cat_dir, "compare_3.png"))
    gen_compare_4(os.path.join(cat_dir, "compare_4.png"))
    
    brands_dir = os.path.join(base_dir, "brands")
    gen_rog_prod_1(os.path.join(brands_dir, "rog_product_1.png"))
    gen_rog_prod_2(os.path.join(brands_dir, "rog_product_2.png"))
    gen_rog_prod_3(os.path.join(brands_dir, "rog_product_3.png"))
    gen_rog_prod_4(os.path.join(brands_dir, "rog_product_4.png"))
    
    gen_apple_prod_1(os.path.join(brands_dir, "apple_product_1.png"))
    gen_apple_prod_2(os.path.join(brands_dir, "apple_product_2.png"))
    gen_apple_prod_3(os.path.join(brands_dir, "apple_product_3.png"))
    gen_apple_prod_4(os.path.join(brands_dir, "apple_product_4.png"))
    gen_apple_prod_5(os.path.join(brands_dir, "apple_product_5.png"))
    gen_apple_prod_6(os.path.join(brands_dir, "apple_product_6.png"))
    
    print("All additional tech assets generated successfully!")
